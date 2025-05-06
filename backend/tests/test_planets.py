import pytest
from flask import Flask
from backend import create_app

BASE_URL = '/api/planets'

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestPlanetsAPI:

    def test_get_all_planets(self, client):
        response = client.get(f'{BASE_URL}/')
        assert response.status_code == 200, "Expected 200 OK for GET /api/planets/"
        assert isinstance(response.json, list)

    def test_get_planet_by_id_found(self, client):
        response = client.get(f'{BASE_URL}/1')
        if response.status_code == 404:
            pytest.skip("Planet ID 1 not found in test DB")
        assert response.status_code == 200
        assert 'id' in response.json

    def test_get_planet_by_id_not_found(self, client):
        response = client.get(f'{BASE_URL}/999999')
        assert response.status_code == 404, "Expected 404 for non-existent planet"

    def test_get_planet_stars(self, client):
        response = client.get(f'{BASE_URL}/1/stars')
        if response.status_code == 404:
            pytest.skip("Planet ID 1 not found for star relationship test")
        assert response.status_code == 200
        assert isinstance(response.json, list)

    def test_ai_description(self, client):
        response = client.get(f'{BASE_URL}/1/ai_description')
        if response.status_code == 404:
            pytest.skip("Planet ID 1 not found for AI description test")
        assert response.status_code == 200
        assert 'description' in response.json

    # --- Enhanced Search Tests ---

    @pytest.mark.parametrize("expression,expected_code", [
        ("radius > 0", 200),
        ("mass > 1", 200),
        ("", 400),  # empty string is invalid
        ("DROP TABLE planets;", 400),
        ("radius < 0 AND mass < 0", 200),  # likely to return 0
    ])
    def test_search_expression_variants(self, client, expression, expected_code):
        data = {"request_string": expression}
        response = client.post(f"{BASE_URL}/search", json=data)
        assert response.status_code == expected_code, f"Failed on expression: {expression}"
        if response.status_code == 200:
            assert isinstance(response.json, list)

    def test_search_with_limit_and_offset(self, client):
        data = {"request_string": "radius > 0"}
        response = client.post(f"{BASE_URL}/search?limit=2&offset=0", json=data)
        assert response.status_code == 200
        assert isinstance(response.json, list)
        assert len(response.json) <= 2

        response2 = client.post(f"{BASE_URL}/search?limit=1&offset=1", json=data)
        assert response2.status_code == 200
        assert isinstance(response2.json, list)

    def test_search_with_large_limit(self, client):
        data = {"request_string": "radius > 0"}
        response = client.post(f"{BASE_URL}/search?limit=9999", json=data)
        assert response.status_code == 200
        assert isinstance(response.json, list)

    def test_search_with_bad_query_param_type(self, client):
        data = {"request_string": "radius > 0"}
        response = client.post(f"{BASE_URL}/search?limit=abc", json=data)
        assert response.status_code == 200  # Flask will ignore bad type and use default (None)

    def test_search_missing_json(self, client):
        # Send empty JSON to avoid 415 Unsupported Media Type
        response = client.post(f"{BASE_URL}/search", json={})
        assert response.status_code == 400  # Should still fail due to missing request_string

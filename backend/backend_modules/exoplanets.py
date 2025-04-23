# %%
# Imports
# Note - by including # %%'s, this can be run like a Jupyter notebook (interactive cell by cell) with Jupytext, or as a traditional Python script
import requests as rq
import pandas as pd
import os

# %%
# Function definitions
directory_path = os.path.dirname(
    os.path.abspath(__file__)
)  # Avoids relative path issues when running alone or as a module
cached_api_results_path = f"{directory_path}/data/exoplanets.csv"
api_token_path = f"{directory_path}/tokens/api_token"


def refresh_exoplanet_data() -> None:
    url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv"
    with open(api_token_path, "r") as token_file:
        api_token = token_file.read().strip()

    response = rq.get(url, headers={"Authorization": f"Bearer {api_token}"})

    if response.status_code == 200:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(cached_api_results_path), exist_ok=True)

        with open(cached_api_results_path, "w") as file:
            file.write(response.text)
    else:
        print(f"Error: {response.status_code}")


def get_exoplanet_data(refresh: bool = False) -> pd.DataFrame:
    if refresh or not os.path.exists(cached_api_results_path):
        refresh_exoplanet_data()
    return pd.read_csv(cached_api_results_path)


# %%

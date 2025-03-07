# %%
import requests as rq
import polars as pl

# %%
url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&format=csv"
with open("api_token", "r") as token_file:
    api_token = token_file.read().strip()

response = rq.get(url, headers={"Authorization": f"Bearer {api_token}"})

# %%
if response.status_code == 200:
    with open("exoplanets.csv", "w") as file:
        file.write(response.text)
else:
    print(f"Error: {response.status_code}")
# %%
df = pl.read_csv("exoplanets.csv")

# %%

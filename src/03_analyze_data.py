import requests
import pandas as pd
medicare = requests.get("https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data")
medicare = pd.DataFrame(medicare.json())
medicare["Tot_Spndng_2024"]=pd.to_numeric(medicare["Tot_Spndng_2024"])
print(medicare[["HCPCS_Cd", "Brnd_Name", "Tot_Spndng_2024"]].sort_values("Tot_Spndng_2024", ascending=False).head())
print(medicare["Tot_Spndng_2024"].dtype)

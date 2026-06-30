import requests
import pandas as pd
pd.set_option("display.max_columns", None)
medicare = requests.get("https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data")
medicare = pd.DataFrame(medicare.json())
medicare["Tot_Spndng_2020"] = pd.to_numeric(medicare["Tot_Spndng_2020"])
medicare["Tot_Spndng_2024"] = pd.to_numeric(medicare["Tot_Spndng_2024"])
# medicare["spending_growth"] = ((medicare["Tot_Spndng_2024"] - medicare["Tot_Spndng_2020"]) / medicare["Tot_Spndng_2020"]) * 100
medicare["spending_growth"] = (medicare["Tot_Spndng_2024"] - medicare["Tot_Spndng_2020"])
print(medicare[["HCPCS_Cd", "Brnd_Name", "Tot_Spndng_2020", "Tot_Spndng_2024", "spending_growth"]].sort_values("spending_growth", ascending = False).head())
# print(medicare[medicare["HCPCS_Cd"] == "90658"][["Brnd_Name", "Tot_Spndng_2020", "Tot_Spndng_2024", "spending_growth"]])

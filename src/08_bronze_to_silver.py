import boto3
import pandas as pd
import io

s3 = boto3.client("s3")

obj = s3.get_object(
        Bucket = "ecommerce-pipeline-bronze-460678531249",
        Key="healthcare/raw/medicare_drug_spending.csv"
        )

medicare = pd.read_csv(io.BytesIO(obj["Body"].read()))
print("Downloaded from S3 successfully!")
print(medicare.shape)

medicare["Tot_Spndng_2020"] = pd.to_numeric(medicare["Tot_Spndng_2020"])
medicare["Tot_Spndng_2021"] = pd.to_numeric(medicare["Tot_Spndng_2021"])
medicare["Tot_Spndng_2022"] = pd.to_numeric(medicare["Tot_Spndng_2022"])
medicare["Tot_Spndng_2023"] = pd.to_numeric(medicare["Tot_Spndng_2023"])
medicare["Tot_Spndng_2024"] = pd.to_numeric(medicare["Tot_Spndng_2024"])
medicare["is_new_drug"] = medicare["Tot_Spndng_2020"].isna()
medicare["spending_growth"] = ((medicare["Tot_Spndng_2021"] - medicare["Tot_Spndng_2020"]) / medicare["Tot_Spndng_2020"]) * 100

print(medicare.shape)
print(medicare.head(10))

medicare.to_csv("../data/processed/medicare_drug_spending.csv", index=False)



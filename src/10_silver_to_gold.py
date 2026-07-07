import boto3
import pandas as pd
import io

s3 = boto3.client("s3")

obj = s3.get_object(
        Bucket = "ecommerce-pipeline-bronze-460678531249",
        Key="healthcare/silver/medicare_drug_spending_clean.csv"
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

top10 = medicare[["HCPCS_Cd", "Brnd_Name", "Tot_Spndng_2024"]].sort_values("Tot_Spndng_2024", ascending=False).head(10)

yearly_spending = {
    "2020": medicare["Tot_Spndng_2020"].sum(),
    "2021": medicare["Tot_Spndng_2021"].sum(),
    "2022": medicare["Tot_Spndng_2022"].sum(),
    "2023": medicare["Tot_Spndng_2023"].sum(),
    "2024": medicare["Tot_Spndng_2024"].sum(),
}

new_drugs_count = medicare["is_new_drug"].value_counts()

avg_spend_per_beneficiary_2024 = medicare["Avg_Spndng_Per_Bene_2024"].mean()

print("Top 10 barnds of 2024:\n", top10)
print("yearly spending:\n", yearly_spending)
print(new_drugs_count)
print("average spend per beneficiary in 2024:\n", avg_spend_per_beneficiary_2024)


# Save to local reports folder
top10.to_csv("../data/reports/top10_drugs_2024.csv", index=False)

yearly_df = pd.DataFrame(list(yearly_spending.items()), columns=["year", "total_spending"])
yearly_df.to_csv("../data/reports/yearly_spending.csv", index=False)

new_drugs_df = new_drugs_count.reset_index()
new_drugs_df.columns = ["is_new_drug", "count"]
new_drugs_df.to_csv("../data/reports/new_vs_existing.csv", index=False)

print("Saved all reports locally!")

# Upload to S3 Gold layer
s3.upload_file("../data/reports/top10_drugs_2024.csv", "ecommerce-pipeline-bronze-460678531249", "healthcare/gold/top10_drugs_2024.csv")
s3.upload_file("../data/reports/yearly_spending.csv", "ecommerce-pipeline-bronze-460678531249", "healthcare/gold/yearly_spending.csv")
s3.upload_file("../data/reports/new_vs_existing.csv", "ecommerce-pipeline-bronze-460678531249", "healthcare/gold/new_vs_existing.csv")

print("Uploaded all Gold layer files to S3!")

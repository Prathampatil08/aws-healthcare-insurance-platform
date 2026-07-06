import boto3
BUCKET = "ecommerce-pipeline-bronze-460678531249"
s3 = boto3.client("s3")
s3.upload_file(
        "/home/pratham08/projects/aws-healthcare-insurance-platform/data/processed/medicare_drug_spending.csv",
        "ecommerce-pipeline-bronze-460678531249",
        "healthcare/silver/medicare_drug_spending_clean.csv"
        )

print("uploaded succesfully")

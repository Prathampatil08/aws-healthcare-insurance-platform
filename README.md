# 🏥 AWS Healthcare Insurance Analytics Pipeline

A data engineering pipeline that analyzes **Medicare Part B Drug Spending** 
data from the US government, built using Python, pandas, boto3, and AWS S3.

---

## 📊 Dataset

- **Source:** [CMS Medicare Part B Drug Spending](https://data.cms.gov)
- **API:** `https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data`
- **Size:** 799 drugs × 48 columns (2020-2024 spending data)

---

## 🏗️ Architecture

CMS Government API
↓
Bronze Layer (Raw Data)
s3://bucket/healthcare/raw/
↓
Silver Layer (Cleaned Data)
s3://bucket/healthcare/silver/
↓
Gold Layer (Business Metrics)
s3://bucket/healthcare/gold/

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core programming language |
| pandas | Data manipulation and analysis |
| boto3 | AWS SDK — connect Python to AWS |
| AWS S3 | Cloud storage for all 3 layers |
| Git/GitHub | Version control |
| Linux/WSL | Development environment |

---

## 🔍 Key Findings

- **Top drug 2024:** Keytruda (cancer immunotherapy) — $5.98 billion
- **Medicare spending growth:** $37.7B (2020) → $60.8B (2024) — **61% increase in 4 years**
- **New drugs:** 231 drugs launched after 2020 (29% of all drugs) — many COVID-related
- **Average spend per patient:** $48,110 per beneficiary in 2024

---

## 📁 Project Structure

aws-healthcare-insurance-platform/
├── src/
│   ├── 01_basics.py              # Python fundamentals
│   ├── 02_fetch_data.py          # Fetch data from CMS API
│   ├── 03_analyze_data.py        # Sort and filter analysis
│   ├── 04_spending_growth.py     # Calculate spending growth
│   ├── 05_load_and_analyze.py    # Load from CSV
│   ├── 07_upload_to_s3.py        # Upload Bronze layer to S3
│   ├── 08_bronze_to_silver.py    # Clean and validate data
│   └── 09_silver_to_gold.py      # Aggregate business metrics
├── data/
│   ├── raw/                      # Bronze layer (local)
│   ├── processed/                # Silver layer (local)
│   └── reports/                  # Gold layer (local)
└── README.md

---

## 🚀 How to Run

### Prerequisites
- Python 3.12+
- AWS CLI configured (`aws configure`)
- Required libraries: `pip install requests pandas boto3`

### Steps

**1. Fetch raw data from CMS API:**
```bash
python3 src/02_fetch_data.py
```

**2. Upload to S3 Bronze layer:**
```bash
python3 src/07_upload_to_s3.py
```

**3. Clean data (Bronze → Silver):**
```bash
python3 src/08_bronze_to_silver.py
```

**4. Generate business metrics (Silver → Gold):**
```bash
python3 src/09_silver_to_gold.py
```

---

## 📈 Results

### Medicare Spending by Year (All Drugs)
| Year | Total Spending |
|------|---------------|
| 2020 | $37.7 billion |
| 2021 | $40.1 billion |
| 2022 | $44.2 billion |
| 2023 | $50.7 billion |
| 2024 | $60.8 billion |

### Top 5 Drugs by 2024 Spending
| Drug | Spending 2024 |
|------|--------------|
| Keytruda | $5.98B |
| Darzalex Faspro | $2.53B |
| Prolia | $2.43B |
| Eylea | $2.37B |
| Opdivo | $1.93B |

---

## 👨‍💻 Author

**Pratham Patil** — Data Engineer
- GitHub: [@Prathampatil08](https://github.com/Prathampatil08)



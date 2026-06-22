# data_ingestion.py

import pandas as pd

files = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/raw/02_nav_history.csv",
    "aum_by_fund_house": "data/raw/03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "data/raw/04_monthly_sip_inflows.csv",
    "category_inflows": "data/raw/05_category_inflows.csv",
    "industry_folio_count": "data/raw/06_industry_folio_count.csv",
    "scheme_performance": "data/raw/07_scheme_performance.csv",
    "investor_transactions": "data/raw/08_investor_transactions.csv",
    "portfolio_holdings": "data/raw/09_portfolio_holdings.csv",
    "benchmark_indices": "data/raw/10_benchmark_indices.csv"
}

for name, file in files.items():
    print("\n" + "="*50)
    print(f"Dataset: {name}")
    print("="*50)

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(df['fund_house'].unique())

print("\nNumber of Fund Houses:")
print(df['fund_house'].nunique())

print("\nCategories:")
print(df['category'].value_counts())

print("\nRisk Grades:")
print(df.columns.tolist())

print("\nRisk Grades:")
# print(df['risk_grade'].value_counts())

print("\nColumns:")
print(df.columns.tolist())

print(df['risk_category'].value_counts())

import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data["data"])

print(nav_df.head())

nav_df.to_csv(
    "data/raw/hdfc_top100_nav.csv",
    index=False
)

print("NAV data saved successfully!")

import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in schemes.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    file_path = f"data/raw/{fund_name}.csv"

    nav_df.to_csv(file_path, index=False)

    print(f"Saved: {file_path}")

print("\nAll NAV files downloaded successfully!")
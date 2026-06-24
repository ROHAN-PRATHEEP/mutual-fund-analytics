import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
category = pd.read_csv("data/raw/05_category_inflows.csv")
folio = pd.read_csv("data/raw/06_industry_folio_count.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
holdings = pd.read_csv("data/raw/09_portfolio_holdings.csv")
benchmark = pd.read_csv("data/raw/10_benchmark_indices.csv")

datasets = {
    "fund_master": fund_master,
    "nav_history": nav_history,
    "aum": aum,
    "sip": sip,
    "category": category,
    "folio": folio,
    "performance": performance,
    "transactions": transactions,
    "holdings": holdings,
    "benchmark": benchmark
}

for name, df in datasets.items():
    print("\n" + "="*50)
    print(name)
    print("="*50)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nShape:")
print(df.shape)

# Handle missing YoY growth values
sip["yoy_growth_pct"] = sip["yoy_growth_pct"].fillna(0)

print("Missing values after cleaning:")
print(sip.isnull().sum())

import os

os.makedirs("data/processed", exist_ok=True)

fund_master.to_csv("data/processed/fund_master_clean.csv", index=False)
nav_history.to_csv("data/processed/nav_history_clean.csv", index=False)
aum.to_csv("data/processed/aum_clean.csv", index=False)
sip.to_csv("data/processed/sip_clean.csv", index=False)
category.to_csv("data/processed/category_clean.csv", index=False)
folio.to_csv("data/processed/folio_clean.csv", index=False)
performance.to_csv("data/processed/performance_clean.csv", index=False)
transactions.to_csv("data/processed/transactions_clean.csv", index=False)
holdings.to_csv("data/processed/holdings_clean.csv", index=False)
benchmark.to_csv("data/processed/benchmark_clean.csv", index=False)

print("All cleaned datasets saved successfully!")
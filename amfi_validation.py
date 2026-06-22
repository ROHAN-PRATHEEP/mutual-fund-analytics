import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

missing_codes = fund_codes - nav_codes

print("Total Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

print("\nMissing AMFI Codes:", len(missing_codes))

if len(missing_codes) == 0:
    print("✅ All AMFI codes exist in NAV History")
else:
    print("❌ Missing Codes:")
    print(missing_codes)
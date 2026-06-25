import pandas as pd
from sqlalchemy import create_engine
import os

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Folder containing cleaned CSV files
folder = "data/processed"

# Load every cleaned CSV into SQLite
for file in os.listdir(folder):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "").replace("_clean", "")

        df = pd.read_csv(os.path.join(folder, file))

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {table_name}")

print("\n✅ SQLite database created successfully!")
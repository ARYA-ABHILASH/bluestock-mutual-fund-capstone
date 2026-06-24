import shutil

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    shutil.copy(
        f"data/raw/{file}",
        f"data/processed/{file.replace('.csv', '_clean.csv')}"
    )

print("Additional datasets copied successfully!")
import pandas as pd

# =====================================
# 1. CLEAN NAV HISTORY
# =====================================

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort by fund and date
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Forward fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Keep only positive NAV values
nav = nav[nav["nav"] > 0]

# Save cleaned file
nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV cleaned successfully")


# =====================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================

tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Convert date
tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

# Standardize transaction type
tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

tx["transaction_type"] = tx[
    "transaction_type"
].replace({
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
})

# Keep positive transaction amounts
tx = tx[tx["amount_inr"] > 0]

# Check KYC values
print("\nKYC Status Values:")
print(tx["kyc_status"].unique())

# Save cleaned file
tx.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")


# =====================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Convert expense ratio column
perf["expense_ratio_pct"] = pd.to_numeric(
    perf["expense_ratio_pct"],
    errors="coerce"
)

# Keep valid expense ratios
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

# Save cleaned file
perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")

print("\nDay 2 Data Cleaning Completed Successfully!")
# Data Dictionary

## 01_fund_master.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | Text | Mutual fund scheme name |
| fund_house | Text | Fund management company |
| category | Text | Fund category |

---

## 02_nav_history.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| amfi_code | Integer | Scheme code |
| date | Date | NAV date |
| nav | Decimal | Net Asset Value |

---

## 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| return_1yr_pct | Decimal | 1 Year Return |
| return_3yr_pct | Decimal | 3 Year Return |
| return_5yr_pct | Decimal | 5 Year Return |
| expense_ratio_pct | Decimal | Expense Ratio |
| aum_crore | Decimal | Assets Under Management |

---

## 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|----------|-------------|
| investor_id | Text | Investor Identifier |
| transaction_type | Text | SIP/Lumpsum/Redemption |
| amount_inr | Decimal | Transaction Amount |
| transaction_date | Date | Transaction Date |
| kyc_status | Text | Verification Status |

Source: Bluestock Fintech Mutual Fund Analytics Dataset
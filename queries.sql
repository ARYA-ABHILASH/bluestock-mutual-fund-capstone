-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Maximum NAV
SELECT MAX(nav) AS max_nav
FROM fact_nav;

-- 4. Minimum NAV
SELECT MIN(nav) AS min_nav
FROM fact_nav;

-- 5. Transaction count by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 6. Total transaction amount by state
SELECT state, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 7. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 8. Average 1-year return
SELECT AVG(return_1yr_pct) AS avg_return
FROM fact_performance;

-- 9. Top 5 funds by 5-year return
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 10. Count funds by category
SELECT category, COUNT(*) AS fund_count
FROM fact_performance
GROUP BY category;
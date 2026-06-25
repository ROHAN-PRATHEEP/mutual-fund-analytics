-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by month
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM nav_history
GROUP BY month;

-- 3. Total SIP amount
SELECT SUM(sip_inflow_crore)
FROM sip;

-- 4. Number of funds by category
SELECT category, COUNT(*)
FROM fund_master
GROUP BY category;

-- 5. Total transactions by state
SELECT state, COUNT(*)
FROM transactions
GROUP BY state;

-- 6. Average 1-Year Return
SELECT AVG(return_1yr_pct)
FROM performance;

-- 7. Highest Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM performance
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 8. Total Holdings
SELECT COUNT(*)
FROM holdings;

-- 9. Latest NAV Date
SELECT MAX(date)
FROM nav_history;

-- 10. Average AUM
SELECT AVG(aum_crore)
FROM aum;
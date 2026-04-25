#Total Sales by Customer
SELECT Customer, SUM(Amount) AS total_sales
FROM processed
GROUP BY Customer
ORDER BY total_sales DESC;

#Monthly Order Volume and Revenue
SELECT date_format(CAST(OrderDate AS DATE), '%Y-%m') AS order_month,
       COUNT(OrderID) AS total_orders,
       SUM(Amount) AS total_revenue
FROM processed
GROUP BY date_format(CAST(OrderDate AS DATE), '%Y-%m')
ORDER BY order_month;

#Order Status Dashboard
SELECT Status, COUNT(OrderID) AS total_orders
FROM processed
GROUP BY Status
ORDER BY total_orders DESC;

#Average Order Value (AOV) per Customer
SELECT Customer, AVG(Amount) AS avg_order_value
FROM processed
GROUP BY Customer
ORDER BY avg_order_value DESC;

#Top 10 Largest Orders in February 2025
SELECT OrderID, Customer, Amount, OrderDate
FROM processed
WHERE month(CAST(OrderDate AS DATE)) = 2
  AND year(CAST(OrderDate AS DATE)) = 2025
ORDER BY Amount DESC
LIMIT 10;

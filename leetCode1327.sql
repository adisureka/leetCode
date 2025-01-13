# Write your MySQL query statement below

SELECT product_name, sum(unit) AS unit FROM Products
JOIN Orders ON Orders.product_id = Products.product_id
WHERE year(order_date) = 2020 AND month(order_date) =  2
GROUP BY product_name
HAVING unit >= 100
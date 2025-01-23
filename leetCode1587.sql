# Write your MySQL query statement below

SELECT name AS NAME, sum(amount) AS BALANCE FROM Users
JOIN Transactions ON Transactions.account = Users.account
GROUP BY name
HAVING BALANCE > 10000
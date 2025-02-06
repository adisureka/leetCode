# Write your MySQL query statement below

# how dp I add the month column that is needed in the output? - USE date_format
# use concat- but concat you loose the "0" of the first month
# SELECT concat(year(trans_date), "-", month(trans_date)) AS month, country, count(id) as trans_count, count("approved") as approved_count # sum(amount) 

SELECT date_format(trans_date, "%Y-%m") AS month, country, 
count(id) as trans_count, 
sum(
    CASE
        WHEN state = "approved" THEN 1
        ELSE 0
    END) AS approved_count, 
sum(amount) AS trans_total_amount,
sum(
    CASE
        WHEN state = "approved" THEN amount
        ELSE 0
    END
) AS approved_total_amount
FROM Transactions
GROUP BY month, country
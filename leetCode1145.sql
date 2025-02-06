# Write your MySQL query statement below

SELECT sale_date, 
sum(
    CASE
        WHEN fruit = "apples" then sold_num
        ELSE sold_num * -1
    END) AS diff

FROM Sales
GROUP BY sale_date
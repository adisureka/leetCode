# Write your MySQL query statement below

SELECT query_name, 
# FROM Queries
round(sum(rating/position)/count(rating),2)As Quality,
round(sum(
    CASE WHEN rating < 3 THEN 1
          ELSE 0
    END)/count(rating) * 100,2)
AS poor_query_percentage 
FROM Queries
GROUP BY query_name
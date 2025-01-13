-- Write your PostgreSQL query statement below

SELECT activity_date AS day, count(distinct(user_id)) AS active_users FROM Activity
GROUP BY activity_date
HAVING datediff('2019-07-27', day) BETWEEN 0 AND 29
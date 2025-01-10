# Write your MySQL query statement below

SELECT tomorrow.id AS Id FROM Weather AS today
JOIN Weather AS tomorrow
ON tomorrow.temperature > today.temperature AND datediff(tomorrow.recordDate, today.recordDate) = 1

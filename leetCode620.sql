# Write your MySQL query statement below

# Solution without sub query
# SELECT * FROM Cinema
# WHERE description != "boring" and id % 2 != 0
# ORDER BY rating DESC

# Solution 2
SELECT * FROM Cinema
WHERE id NOT IN
(SELECT id FROM Cinema
WHERE description = "boring") AND id % 2 = 1
ORDER BY rating DESC

# Solution 1
-- SELECT * FROM Cinema
-- WHERE description NOT IN (
-- SELECT description FROM Cinema
-- WHERE description = "boring") 
-- AND id NOT IN (SELECT id FROM Cinema
-- WHERE id % 2 = 0)
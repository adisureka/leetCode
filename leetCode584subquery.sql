# Write your MySQL query statement below

# SELECT name FROM Customer
# WHERE referee_id != 2 OR referee_id IS null

# SELECT id FROM Customer
# WHERE referee_id = 2

SELECT name FROM Customer
WHERE id NOT IN (SELECT id FROM Customer WHERE referee_id = 2)
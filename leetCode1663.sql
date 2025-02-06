# Write your MySQL query statement below

SELECT contest_id, round(count(u.user_id)/(SELECT count(user_id) FROM Users) * 100, 2) AS percentage FROM Users u
JOIN Register r ON r.user_id = u.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

-- SELECT contest_id, round(count(u.user_id)/(SELECT count(user_id) FROM Users) * 100, 2) FROM Users u
-- JOIN Register r ON r.user_id = u.user_id
-- GROUP BY contest_id
-- ORDER BY contest_id

-- SELECT contest_id, round(count(distinct(r.user_id))/
-- (SELECT count(user_name) FROM Users) * 100, 2) AS percentage

-- -- SELECT contest_id, (count(r.user_id)/count(user_name)) * 100 AS percentage

-- FROM Register r
-- JOIN Users u ON u.user_id = r.user_id
-- GROUP BY contest_id
-- ORDER BY percentage DESC, contest_id ASC


# WHERE contest_id = 215

-- SELECT contest_id, 
-- # (count(distinct(u.user_id))/count(u.user_id)) * 100 

-- FROM Register r
-- JOIN Users u ON r.user_id = u.user_id
-- GROUP BY contest_id

-- ORDER BY percentage DESC
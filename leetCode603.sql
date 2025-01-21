# Write your MySQL query statement below

# SELECT * FROM Cinema
# WHERE seat_id not in (SELECT seat_id FROM Cinema WHERE free = 0)

SELECT seat_id FROM CInema
WHERE (seat_id - 1 in
(SELECT seat_id FROM Cinema
WHERE free = 1) 
OR seat_id + 1 in (SELECT seat_id FROM Cinema
WHERE free = 1)) AND seat_id not in (SELECT seat_id FROM Cinema WHERE free = 0)
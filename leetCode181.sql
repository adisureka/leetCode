# Write your MySQL query statement below

SELECT manager.name AS Employee FROM Employee AS E1
JOIN Employee AS manager
ON E1.id = manager.managerId
WHERE manager.salary > E1.salary
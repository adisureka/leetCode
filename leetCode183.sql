# Write your MySQL query statement below
# SELECT * FROM Customers
# JOIN Orders on Orders.id != Customers.id

# SELECT * FROM Customers
# WHERE id NOT IN (3,1)


SELECT name AS Customers FROM Customers
WHERE id NOT IN (SELECT customerId FROM Orders)
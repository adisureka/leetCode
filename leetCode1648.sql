# Write your MySQL query statement below

WITH rate_table as 
(SELECT 
    company_id, max(salary),
    (CASE
        WHEN max(salary) < 1000 THEN 0
        WHEN max(salary) > 1000 AND max(salary) < 10000 THEN 0.24
        ELSE 0.49
    END) AS tax_rate
FROM Salaries
GROUP BY company_id)

SELECT Salaries.company_id, employee_id, employee_name, round(salary - (salary * tax_rate), 0) as salary FROM rate_table
JOIN Salaries ON Salaries.company_id = rate_table.company_id

# Write your MySQL query statement below

SELECT id,  
sum(CASE
    WHEN month = "Jan" THEN revenue
END) AS Jan_revenue,
sum(CASE
    WHEN month = "Feb" THEN revenue
END) AS Feb_revenue,
sum(CASE
    WHEN month = "Mar" THEN revenue
END) AS Mar_revenue,
sum(CASE
    WHEN month = "Apr" THEN revenue
END) AS Apr_revenue,
sum(CASE
    WHEN month = "May" THEN revenue
END) AS May_revenue,
sum(CASE
    WHEN month = "Jun" THEN revenue
END) AS Jun_revenue,
sum(CASE
    WHEN month = "Jul" THEN revenue
END) AS Jul_revenue,
sum(CASE
    WHEN month = "Aug" THEN revenue
END) AS Aug_revenue,
sum(CASE
    WHEN month = "Sep" THEN revenue
END) AS Sep_revenue,
sum(CASE
    WHEN month = "Oct" THEN revenue
END) AS Oct_revenue,
sum(CASE
    WHEN month = "Nov" THEN revenue
END) AS Nov_revenue,
sum(CASE
    WHEN month = "Dec" THEN revenue
END) AS Dec_revenue
FROM Department
GROUP BY id

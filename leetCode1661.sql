# Write your MySQL query statement below

SELECT machine_id
 , round(sum(
       CASE WHEN activity_type = "start" THEN -timestamp
            WHEN activity_type = "end" THEN +timestamp
        END)/count(distinct(process_id)),3) AS processing_time 
FROM Activity
GROUP BY machine_id
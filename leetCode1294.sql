# Write your MySQL query statement below

SELECT country_name,
(CASE 
    WHEN avg(weather_state) <= 15 THEN "Cold"
    WHEN avg(weather_state) >= 25 THEN "Hot"
    ELSE "Warm"
    END
) as weather_type 

FROM Countries
JOIN Weather ON Weather.country_id = Countries.country_id
WHERE year(day) = 2019 AND month(day) = 11
GROUP BY country_name
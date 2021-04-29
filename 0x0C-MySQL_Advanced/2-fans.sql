-- SQL script that creates a table users
-- In and not out

SELECT origin as origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
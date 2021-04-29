-- SQL script that creates a table users
-- In and not out
select band_name,
CASE
    WHEN split IS NULL then (2020 - formed)
    ELSE split - formed
END AS lifespan
FROM metal_bands
where style LIKE "%Glam rock%"
ORDER BY lifespan DESC;

-- Second method
/*
SELECT
  band_name AS band_name,
  IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
from
  metal_bands
WHERE
  style LIKE '%Glam rock%'
  */
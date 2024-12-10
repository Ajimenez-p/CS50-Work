-- Find 10 lowest 0m temps
SELECT MIN("0m"), "latitude", "longitude" FROM normals
-- Sort highest to lowest
ORDER BY "Om" ASC, "latitude" ASC
LIMIT 10;

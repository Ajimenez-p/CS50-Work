-- Find 10 highest 0m temps
SELECT MAX("0m"), "latitude", "longitude" FROM normals
-- Sort highest to lowest
ORDER BY "Om" DESC, "latitude" ASC
-- If same values, sort by latitude small to large
LIMIT 10;

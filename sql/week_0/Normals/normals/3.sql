SELECT '0m' FROM normals
WHERE longitude = 50
AND latitude = -30

UNION ALL

SELECT '100m' FROM normals
WHERE longitude = 50 AND latitude = -30

UNION ALL

SELECT '200m' FROM normals
WHERE longitude = 50
AND latitude = -30;

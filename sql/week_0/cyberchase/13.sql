SELECT "production_code" FROM "episodes"
WHERE "air_date" BETWEEN '2006-01-01' AND '2024-10-18'
AND "episode_in_season" = 5 OR 6;

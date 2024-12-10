
-- *** The Lost Letter ***
-- getting idea of tables
SELECT * FROM "addresses"
LIMIT 5;

SELECT * FROM "drivers"
LIMIT 5;

SELECT * FROM "packages"
LIMIT 5;

SELECT * FROM "scans"
LIMIT 5;

-- goal is to find status of package. first we find what package it is
-- first, we'll use addresses to determine which package id it is
SELECT "id" FROM "addresses"
WHERE "address" LIKE '%Somerville%'
OR "address" LIKE '%Finnegan%'; -- this returns ID 432

SELECT * FROM "packages"
WHERE "from_address_id" = 432; -- returns ID 384 (package) going to 854

SELECT * from "scans"
WHERE "package_id" = 384 --gets things not in order, let's take a look in order of date
ORDER BY "timestamp" DESC;

-- last one gives us status as dropped off on July 11th, 2023 @ 11pm

-- *** The Devious Delivery ***
-- town = Fiftyville, probably a duck for contents
-- no From address
SELECT * FROM "addresses"
LIMIT 5; --get an idea of addresses again

-- addresses won't be helpful yet. let's try to find the package based on no "From" address
SELECT * FROM "packages"
WHERE "from_address_id" IS NULL; --returns Package ID 5098, to_address_id 50

SELECT * FROM "scans"
WHERE "package_id" = 5098
ORDER BY "timestamp" DESC; --status of his package

--was delivered to the wrong address:
SELECT "address" from "addresses"
WHERE "id" = 348;

--sent to 7 Humboldt Place, Police Station

-- *** The Forgotten Gift ***
-- sent to 728 Maple Place, sent from 109 Tileston Street

--find address IDs
SELECT * FROM "addresses"
WHERE "address" LIKE '%MAPLE%'
OR "address" LIKE '%TILESTON%';

--too vague, need to filter it further
SELECT * FROM "addresses"
WHERE "address" LIKE '728 MAPLE%'
OR "address" LIKE '109 TILESTON%';
--returns 4983 for maple & 9873 for tileston

SELECT * FROM packages
WHERE "from_address_id" = 9873
AND "to_address_id" = 4983; --gets package ID 9523

SELECT * FROM scans
WHERE package_id = 9523
ORDER BY timestamp DESC; --current status is picked up by driver 17

SELECT * from drivers
WHERE id = 17; --gives us Mikel

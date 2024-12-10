/* Another parent wants to send their child to a district with few other students. In 9.sql,
write a SQL query to find the name (or names) of the school district(s) with the single least number of
pupils. Report only the name(s). */

SELECT districts.name FROM districts
RIGHT JOIN expenditures ON districts.id = expenditures.district_id
GROUP BY districts.name
ORDER BY expenditures.pupils ASC;

/* Is there a relationship between school expenditures and graduation rates? In 11.sql, write a SQL
query to display the names of schools, their per-pupil expenditure, and their graduation rate. Sort the
 schools from greatest per-pupil expenditure to least. If two schools have the same per-pupil expenditure,
 sort by school name.

    You should assume a school spends the same amount per-pupil their district as a whole spends.

*/

SELECT schools.name, expenditures.per_pupil_expenditure, graduation_rates.graduated from schools
INNER JOIN expenditures ON schools.district_id = expenditures.district_id
INNER JOIN graduation_rates ON schools.id = graduation_rates.school_id
ORDER BY expenditures.per_pupil_expenditure DESC, schools.name ASC;

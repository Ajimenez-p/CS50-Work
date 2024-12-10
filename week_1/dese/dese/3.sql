SELECT AVG(per_pupil_expenditure) AS 'Average District Per-Pupil Expenditure'
FROM expenditures
INNER JOIN districts ON expenditures.district_id = districts.id;

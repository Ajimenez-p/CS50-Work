SELECT districts.name, expenditures.per_pupil_expenditure, grad_data.dropped FROM districts
INNER JOIN expenditures ON districts.id = expenditures.district_id
INNER JOIN (
    SELECT graduation_rates.dropped, schools.district_id
    FROM graduation_rates
    INNER JOIN schools ON graduation_rates.school_id = schools.id
) AS grad_data ON grad_data.district_id = districts.id
ORDER BY expenditures.per_pupil_expenditure DESC, grad_data.dropped DESC
LIMIT 10;


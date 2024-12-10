/*
Your general manager (i.e., the person who makes decisions about player contracts) asks you
whether the team should trade a current player for Cal Ripken Jr., a star player who’s likely
nearing his retirement. In 2.sql, write a SQL query to find Cal Ripken Jr.’s salary history.

    Sort by year in descending order.
    Your query should return a table with two columns, one for year and one for salary.

*/

SELECT salaries.year, salaries.salary FROM salaries
WHERE player_id = (
        SELECT id from players
        WHERE first_name = 'Cal'
        AND last_name = 'Ripken')
GROUP BY salaries.year
ORDER BY salaries.year DESC;

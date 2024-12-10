/* How much would the A’s need to pay to get the best home run hitter this past season? In 8.sql,
write a SQL query to find the 2001 salary of the player who hit the most home runs in 2001.

    Your query should return a table with one column, the salary of the player.
*/

SELECT salaries.salary FROM salaries
INNER JOIN players ON salaries.player_id = players.id
WHERE salaries.year = 2001
ORDER BY salaries.salary DESC
LIMIT 1;

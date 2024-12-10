-- Satchel Paige, find all teams, 1 column w/ names of teams

-- 3. Use the team IDs to list all team names
SELECT DISTINCT teams.name FROM teams
JOIN performances ON teams.id = performances.team_id
WHERE performances.player_id = (
    -- 1. Find Satchel Paige's player_id
    SELECT players.id FROM players
    WHERE players.first_name LIKE 'Satchel'
    AND players.last_name LIKE 'Paige'
);

WITH Players AS (
    SELECT
        player_id,
        MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT
    ROUND(
        COUNT(Players.player_id) /
        (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    ) AS fraction
FROM Players
JOIN Activity
    ON Players.player_id = Activity.player_id
    AND DATEDIFF(Activity.event_date, Players.first_login) = 1;

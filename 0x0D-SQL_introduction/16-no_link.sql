-- lists every record in my MySQL server's second_table that has a name value.
-- records are arranged by descending score
SELECT 'score', 'name'
FROM 'second_table'
WHERE 'name' != ""
ORDER BY 'score' DESC;

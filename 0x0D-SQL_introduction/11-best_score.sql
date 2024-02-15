-- lists every record in MySQL server's second_table that has a score of >= 10
-- records are arranged by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

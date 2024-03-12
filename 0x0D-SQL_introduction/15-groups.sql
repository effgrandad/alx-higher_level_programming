-- displays the quantity of records in my MySQL server's second_table that have the same score
-- records are arranged by descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

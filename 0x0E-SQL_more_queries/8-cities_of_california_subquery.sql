-- lists every city in California accessible through the database. hbtn 0d usa
-- lists every row in a database for a given column
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;

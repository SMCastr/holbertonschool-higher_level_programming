-- 16-no_link.sql
-- SQL query to list all records of the second_table with a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
-- Exit from MySQL shell
EXIT;
-- 8-cities_of_california_subquery.sql
-- Script to list all cities of California from the 'cities' table in the 'hbtn_0d_usa' database

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Select all cities of California using a subquery
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;

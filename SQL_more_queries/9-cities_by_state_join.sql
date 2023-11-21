-- 9-cities_by_state_join.sql
-- Script to list all cities and their corresponding states from the 'cities' and 'states' tables in the 'hbtn_0d_usa' database

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Select all cities and their corresponding states using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

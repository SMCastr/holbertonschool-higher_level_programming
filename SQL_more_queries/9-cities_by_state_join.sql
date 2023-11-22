-- 9-cities_by_state_join.sql
-- This script creates a table 'cities' in the database

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
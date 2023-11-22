-- 9-cities_by_state_join.sql

-- Select all cities and their corresponding states using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
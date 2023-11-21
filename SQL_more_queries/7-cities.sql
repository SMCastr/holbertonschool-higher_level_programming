-- 7-cities.sql
-- Script to create the database 'hbtn_0d_usa' and the table 'cities' in the database

-- Create or replace the database 'hbtn_0d_usa' if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Create or replace the table 'cities' if it exists
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states (id)
);

-- Optional: Display the structure of the 'cities' table for verification
DESCRIBE cities;

-- Optional: Insert sample data into the 'cities' table
INSERT INTO cities (state_id, name) VALUES
    (1, 'San Francisco');

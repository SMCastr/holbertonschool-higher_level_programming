-- 6-states.sql
-- Script to create the database 'hbtn_0d_usa' and the table 'states' in the database

-- Create or replace the database 'hbtn_0d_usa' if it exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Create or replace the table 'states' if it exists
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Optional: Display the structure of the 'states' table for verification
DESCRIBE states;

-- Optional: Insert sample data into the 'states' table
INSERT INTO states (name) VALUES
    ('California'),
    ('Arizona'),
    ('Texas');

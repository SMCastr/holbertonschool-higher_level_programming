-- 5-unique_id.sql
-- Script to create the table unique_id on the MySQL server

-- Create or replace the table 'unique_id' if it exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Optional: Display the structure of the 'unique_id' table for verification
DESCRIBE unique_id;

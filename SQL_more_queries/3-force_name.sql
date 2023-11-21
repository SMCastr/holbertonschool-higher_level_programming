-- 3-force_name.sql
-- Script to create the table force_name on the MySQL server

-- Create or replace the table 'force_name' if it exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Optional: Display the structure of the 'force_name' table for verification
DESCRIBE force_name;

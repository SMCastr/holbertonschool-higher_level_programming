-- 3-force_name.sql
-- This script creates a table 'force_name' in the database

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
);

-- Optional: Display the structure of the 'unique_id' table for verification
DESCRIBE unique_id;
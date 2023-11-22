-- 4-never_empty.sql
-- Script to create the table id_not_null on the MySQL server

-- Create or replace the table 'id_not_null' if it exists
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
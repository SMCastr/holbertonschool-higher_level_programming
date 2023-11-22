-- 3-force_name.sql
-- Script to create a table 'force_name' in the database

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
);
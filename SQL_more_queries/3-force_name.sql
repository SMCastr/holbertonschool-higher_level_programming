-- 3-force_name.sql
-- Script to create the table force_name
-- This table is used to store the names of the forces
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
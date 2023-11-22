-- 4-never_empty.sql
-- This script creates a table 'id_not_null' in the database

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
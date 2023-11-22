-- 4-never_empty.sql
-- Script to create the database 'hbtn_0d_usa' and the table 'states' in the database

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
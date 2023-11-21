-- 0-privileges.sql
-- Script to list all privileges of MySQL users on the localhost
-- Ensure that the users exist before checking their privileges
-- Create user 'user_0d_1' if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Grant all privileges to 'user_0d_1' on all databases, tables, etc. (wildcard '*.*')
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Create user 'user_0d_2' if not exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Now, list the privileges for both users
-- List privileges for 'user_0d_1'
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- List privileges for 'user_0d_2'
SHOW GRANTS FOR 'user_0d_2'@'localhost';
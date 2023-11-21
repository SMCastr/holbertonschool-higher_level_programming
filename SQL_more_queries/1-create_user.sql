-- 1-create_user.sql
-- Script to create the MySQL server user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to 'user_0d_1' on all databases, tables, etc. (wildcard '*.*')
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Optional: Display the privileges for 'user_0d_1' for verification
SHOW GRANTS FOR 'user_0d_1'@'localhost';
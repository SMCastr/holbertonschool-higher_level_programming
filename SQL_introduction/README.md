SQL - Introduction
==================
## What is SQL?
SQL stands for Structured Query Language. It is a language used to interact with databases. It is a standard language for relational database management systems (RDBMS). It is particularly useful in handling structured data, i.e. data incorporating relations among entities and variables.

## What is a database?
A database is a collection of data stored in a computer system. Databases can be categorized according to types of content: bibliographic, full-text, numeric, and images. There are several types of databases, such as relational database, object databases, graph databases, network databases, and document databases.

## What is a relational database?
A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points.

# SQL Introduction Project

This project covers various SQL tasks to get hands-on experience with MySQL. The tasks involve creating databases, tables, and performing operations such as inserting, updating, and querying data.

## Table of Contents
1. [List Databases](./0-list_databases.sql)
2. [Create a Database](./1-create_database_if_missing.sql)
3. [Delete a Database](./2-remove_database.sql)
4. [List Tables](./3-list_tables.sql)
5. [First Table](./4-first_table.sql)
6. [Full Description](./5-full_table.sql)
7. [List All in Table](./6-list_values.sql)
8. [First Add](./7-insert_value.sql)
9. [Count 89](./8-count_89.sql)
10. [Full Creation](./9-full_creation.sql)
11. [List by Best](./10-top_score.sql)
12. [Select the Best](./11-best_score.sql)
13. [Cheating is Bad](./12-no_cheating.sql)
14. [Score Too Low](./13-change_class.sql)
15. [Average](./14-average.sql)
16. [Number by Score](./15-groups.sql)
17. [Say My Name](./16-no_link.sql)

## Definitions and Explanations

### 0. List Databases
Lists all databases on the MySQL server.

### 1. Create a Database
Creates the database `hbtn_0c_0` if it doesn't already exist.

### 2. Delete a Database
Deletes the database `hbtn_0c_0` if it exists.

### 3. List Tables
Lists all tables in the specified database.

### 4. First Table
Creates a table called `first_table` in the specified database.

### 5. Full Description
Prints the full description of the `first_table` in the specified database.

### 6. List All in Table
Lists all rows of the `first_table` in the specified database.

### 7. First Add
Inserts a new row into the `first_table` in the specified database.

### 8. Count 89
Displays the number of records with `id = 89` in the `first_table`.

### 9. Full Creation
Creates a table called `second_table` and adds multiple rows to it.

### 10. List by Best
Lists all records of the `second_table` ordered by descending score.

### 11. Select the Best
Lists records with a score >= 10 in the `second_table` ordered by descending score.

### 12. Cheating is Bad
Updates the score of 'Bob' to 10 in the `second_table`.

### 13. Score Too Low
Removes all records with a score <= 5 in the `second_table`.

### 14. Average
Computes the average score of all records in the `second_table`.

### 15. Number by Score
Lists the number of records with the same score in the `second_table`.

### 16. Say My Name
Lists all records of the `second_table` with a name value, ordered by descending score.

## Usage
To run these scripts, use the following command:

```bash
cat script.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

## Author
Sweety Castro

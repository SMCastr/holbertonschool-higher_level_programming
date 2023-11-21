SQL - Introduction
==================
## What is SQL?
SQL stands for Structured Query Language. It is a language used to interact with databases. It is a standard language for relational database management systems (RDBMS). It is particularly useful in handling structured data, i.e. data incorporating relations among entities and variables.

## What is a database?
A database is a collection of data stored in a computer system. Databases can be categorized according to types of content: bibliographic, full-text, numeric, and images. There are several types of databases, such as relational database, object databases, graph databases, network databases, and document databases.

## What is a relational database?
A relational database is a type of database that stores and provides access to data points that are related to one another. Relational databases are based on the relational model, an intuitive, straightforward way of representing data in tables. In a relational database, each row in the table is a record with a unique ID called the key. The columns of the table hold attributes of the data, and each record usually has a value for each attribute, making it easy to establish the relationships among data points.

## What is a relational database management system (RDBMS)?
A relational database management system (RDBMS) is a program that allows you to create, update, and administer a relational database. Most relational database management systems use the SQL language to access the database.

## What does SQL stand for? What is it used for?
SQL stands for Structured Query Language. It is a language used to interact with databases. It is a standard language for relational database management systems (RDBMS). It is particularly useful in handling structured data, i.e. data incorporating relations among entities and variables.

## What’s a primary key? What’s a foreign key? How to link Tables with foreign keys?
A primary key is a column or group of columns in a table that uniquely identify every row in that table. A foreign key is a column or group of columns in a table that links to a primary key in another table. To link tables with foreign keys, you need to create a foreign key in the table that you want to link to the primary key in another table.

## How to create a new database in MySQL?
To create a new database in MySQL, you need to use the CREATE DATABASE statement. The syntax is as follows:
```
CREATE DATABASE database_name;
```
For example, to create a database called `my_database`, you can use the following statement:
```
CREATE DATABASE my_database;
```

## How to create a new table in MySQL?
To create a new table in MySQL, you need to use the CREATE TABLE statement. The syntax is as follows:
```
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
   ....
);
```
For example, to create a table called `my_table` with three columns, `id`, `name`, and `age`, you can use the following statement:
```
CREATE TABLE my_table (
    id INT,
    name VARCHAR(50),
    age INT
);
```

## How to insert a new item in a table?
To insert a new item in a table, you need to use the INSERT INTO statement. The syntax is as follows:
```
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```
For example, to insert a new item into the table `my_table` with the values `1`, `John`, and `25`, you can use the following statement:
```
INSERT INTO my_table (id, name, age)
VALUES (1, 'John', 25);
```

## How to fetch rows from a SQL table?
To fetch rows from a SQL table, you need to use the SELECT statement. The syntax is as follows:
```
SELECT column1, column2, ...
FROM table_name;
```
For example, to fetch all rows from the table `my_table`, you can use the following statement:
```
SELECT * FROM my_table;
```

## How to update rows in a SQL table?
To update rows in a SQL table, you need to use the UPDATE statement. The syntax is as follows:
```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
For example, to update the row with the id `1` in the table `my_table` with the values `2`, `Jane`, and `30`, you can use the following statement:
```
UPDATE my_table
SET id = 2, name = 'Jane', age = 30
WHERE id = 1;
```

## How to delete rows from a SQL table?
To delete rows from a SQL table, you need to use the DELETE statement. The syntax is as follows:
```
DELETE FROM table_name
WHERE condition;
```
For example, to delete the row with the id `1` in the table `my_table`, you can use the following statement:
```
DELETE FROM my_table
WHERE id = 1;
```

## What’s a schema?
A schema is a collection of database objects, including tables, views, indexes, and synonyms. You can create a schema to group database objects together, which makes it easier to manage permissions on those objects.

## What’s a stored procedure?
A stored procedure is a set of SQL statements that are stored in the database server. Stored procedures can be used to perform complex database operations that would otherwise require multiple SQL statements. Stored procedures can also be used to improve performance by reducing network traffic between the application and the database server.

## What’s a trigger?
A trigger is a special type of stored procedure that is automatically executed when a specific event occurs. For example, you can create a trigger that is executed when a new row is inserted into a table. Triggers can be used to enforce business rules, perform data validation, or perform other actions that are not possible with standard SQL statements.

## What are the main differences between SQL and NoSQL?

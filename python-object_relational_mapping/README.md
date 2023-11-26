Python - Object-relational mapping
===================================

# Python Object Relational Mapping (ORM)

This repository contains Python scripts and SQLAlchemy models for performing Object-Relational Mapping (ORM) with MySQL databases. The scripts cover various tasks, including querying, inserting, updating, and deleting data using SQLAlchemy and MySQL databases.

## Files and Descriptions
===================================
### 0-select_states.py
- Script to list all states from the database.
- Usage: `./0-select_states.py <username> <password> <database_name>`

### 1-filter_states.py
- Script to list states with names starting with 'N'.
- Usage: `./1-filter_states.py <username> <password> <database_name>`

### 2-my_filter_states.py
- Script to list states based on user input.
- Usage: `./2-my_filter_states.py <username> <password> <database_name> <state_name>`

### 3-my_safe_filter_states.py
- Script to list states based on user input, with protection against SQL injection.
- Usage: `./3-my_safe_filter_states.py <username> <password> <database_name> <state_name>`

### 4-cities_by_state.py
- Script to list all cities from the database, along with their respective states.
- Usage: `./4-cities_by_state.py <username> <password> <database_name>`

### 5-filter_cities.py
- Script to list all cities of a specific state.
- Usage: `./5-filter_cities.py <username> <password> <database_name> <state_name>`

### 6-model_state.py
- Contains the class definition of the `State` class and an instance of `Base`.
- Used for defining the `states` table in the database.

### 7-model_state_fetch_all.py
- Script to list all `State` objects from the database.
- Usage: `./7-model_state_fetch_all.py <username> <password> <database_name>`

### 8-model_state_fetch_first.py
- Script to print the first `State` object from the database.
- Usage: `./8-model_state_fetch_first.py <username> <password> <database_name>`

### 9-model_state_filter_a.py
- Script to list `State` objects that contain the letter 'a' in their names.
- Usage: `./9-model_state_filter_a.py <username> <password> <database_name>`

### 10-model_state_my_get.py
- Script to print the `State` object with the given name.
- Usage: `./10-model_state_my_get.py <username> <password> <database_name> <state_name>`

### 11-model_state_insert.py
- Script to add the `State` object "Louisiana" to the database.
- Usage: `./11-model_state_insert.py <username> <password> <database_name>`

### 12-model_state_update_id_2.py
- Script to change the name of a `State` object where `id = 2` to "New Mexico".
- Usage: `./12-model_state_update_id_2.py <username> <password> <database_name>`

### 13-model_state_delete_a.py
- Script to delete all `State` objects with a name containing the letter 'a'.
- Usage: `./13-model_state_delete_a.py <username> <password> <database_name>`

### model_city.py
- Contains the class definition of the `City` class, inheriting from `Base`.
- Defines the `cities` table in the database.

### 14-model_city_fetch_by_state.py
- Script to print all `City` objects from the database, organized by state.
- Usage: `./14-model_city_fetch_by_state.py <username> <password> <database_name>`
===================================

## Requirements
- Python 3
- MySQL database
- SQLAlchemy library

## Usage
1. Clone this repository.
2. Navigate to the repository directory.
3. Execute the desired script with the appropriate arguments.

More Info
Install MySQL 8.0 on Ubuntu 20.04 LTS

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$


Feel free to explore and use these scripts for your Object-Relational Mapping tasks!

## Author
* ** Sweety Castro** - [SweetyCastro]

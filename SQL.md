# SQL WIKI

## Intro

**SQL** stands for Structured Query Language and is the language syntax for many _database management systems_

The most common _database management systems_ is **MySQL**, although there are others, including:

- MySQL
- SQLite
- PostgreSQL
- Oracle
- & many more

## setting up

My system at the time:

```
Operating System: Debian GNU/Linux 10 (buster)
Kernel: Linux 4.19.0-6-amd64
Architecture: x86-64
```

### Installing MySQL

```shell
sudo apt-get update
sudo apt-get install default-mysql-server
mysql_secure_installation
```

[ERROR fixes here](https://stackoverflow.com/questions/37879448/mysql-fails-on-mysql-error-1524-hy000-plugin-auth-socket-is-not-loaded?noredirect=1)

Test the instilation:

```shell
systemctl status mysql.service
```

Check admin command:

```shell
mysqladmin -p -u root version
```

### Setting up with Atom

```
apm install autocomplete-sql
```

## Using SQL

SQL uses statements (ending with ;) to execute operations. Statements include

- CLAUSE - (in all caps) to perform specific tasks
- table name
- column name
- row name
- parameters
- DATATYPE - (in all caps)
- CONSTRAINTS - (in all caps)

Types of data include:

- **INTEGER**, a positive or negative whole number
- **TEXT**, a text string
- **DATE**, the date formatted as YYYY-MM-DD
- **REAL**, a decimal value

--------------------------------------------------------------------------------

### Create Table

- **CREATE** - to create a new table

```sql
CREATE TABLE table_name (
  id INTEGER,
  name TEXT,
  age INTEGER
);
```

--------------------------------------------------------------------------------

### Insert Into Table

- **INSERT INTO** - insert a row into the table

```sql
INSERT INTO table_name (id, name, age)
```

--------------------------------------------------------------------------------

### Ulter table

- **ALTER TABLE** - Claus to alter a table
- **ADD COLUMN** - Clause to add a column

```sql
ALTER TABLE table_name
ADD COLUMN new_column_name TEXT;
```

--------------------------------------------------------------------------------

### Update Row

- **UPDATE** - clause that edits a row in the table
- **SET** - clause that indicates the column to edit

```sql
UPDATE table_name
SET new_column_name = 'data to change';
```

--------------------------------------------------------------------------------

### Delete Rows

- **DELETE FROM** - clause that lets you delete rows from a table
- **WHERE** - clause that lets you select which rows you want to delete
- **IS NULL** - condition in SQL that returns true when the value is NULL and false otherwise

```sql
DELETE FROM table_name
WHERE column_name IS NULL;
```

--------------------------------------------------------------------------------

### Constraints

- **PRIMARY KEY** - used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a _constraint violation_
- **UNIQUE** - columns must have a different value for every row
- **NOT NULL** - columns must have a value. Attempts to insert a row without a value for a NOT NULL column will result in a _constraint violation_
- **DEFAULT** - assumed value for an inserted row

```sql
CREATE TABLE table_name (
   id INTEGER PRIMARY KEY,
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```

--------------------------------------------------------------------------------

### Query Table

- **SELECT** - can take multiple columns - `column_name1, column_name2`. Use `*` instead of column_name to get all columns
- **FROM** - identifies the table

```sql
SELECT column_name FROM table_name;
```

--------------------------------------------------------------------------------

- **AS** - to rename the column. The 'New name' should be in single quotes

```sql
SELECT column_name AS 'new name'
FROM table_name;
```

--------------------------------------------------------------------------------

- **DISTINCT** - used to return the unique values in the output

```sql
SELECT DISTINCT column_name
FROM table_name;
```

--------------------------------------------------------------------------------

- **WHERE** - Constraint followed by a Comparison operators that returns True or False Comparison operators include:
- `=` equal to
- `!=` not equal to
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

```sql
SELECT *
FROM table_name
WHERE column_name > 8;
```

--------------------------------------------------------------------------------

- **LIKE** - to compare similar values The pattern is identified by an underscore

Wildcard character:

- _- matches different characters. `data_.csv`will be true for`data1.csv`and`data5.csv`but not`data5.txt`
- % - matches zero or more missing letters in the pattern. `The %` will be true for `The dog` and `The house` but not `A family`

```sql
SELECT *
FROM table_name
WHERE column_name LIKE 'recogni_e';

SELECT *
FROM table_name
WHERE column_name LIKE 'The %';
```

--------------------------------------------------------------------------------

- **IS NULL** - returns true for null values
- **IS NOT NULL** - returns for values that are not null

```sql
SELECT column_name
FROM table_name
WHERE another_column_name IS NOT NULL;
```

--------------------------------------------------------------------------------

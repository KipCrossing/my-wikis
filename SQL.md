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

Types of data include:

- **INTEGER**, a positive or negative whole number
- **TEXT**, a text string
- **DATE**, the date formatted as YYYY-MM-DD
- **REAL**, a decimal value

### Create Table

```sql
CREATE TABLE table_name (
  id INTEGER,
  name TEXT,
  age INTEGER
);
```

### Query Table

```sql
SELECT column_name FROM table_name;
```

Use * instead of column_name to get all columns

### Insert Into Table

```sql
INSERT INTO table_name (id, name, age)
```

### Ulter table

For adding columns

```sql
ALTER TABLE table_name
ADD COLUMN new_column_name TEXT;
```

- `ALTER TABLE` - Claus to alter a table
- `ADD COLUMN` - Clause to add a column

### Update Row

```sql
UPDATE table_name
SET new_column_name = 'data to change'
WHERE id = 4;
```

- `UPDATE` - clause that edits a row in the table
- `SET` - clause that indicates the column to edit
- `WHERE` - clause that indicates which row(s) to update with the new column value

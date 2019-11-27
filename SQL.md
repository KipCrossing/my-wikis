# SQL WIKI

## Intro

**SQL** stands for Structured Query Language and is the language syntax for many _database management systems_

The most common _database management systems_ is **MySQL**, although there are others, including:

- MySQL
- SQLite
- PostgreSQL
- Oracle
- - many more

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

[FRROE fixes here](https://stackoverflow.com/questions/37879448/mysql-fails-on-mysql-error-1524-hy000-plugin-auth-socket-is-not-loaded?noredirect=1)

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
- parameters

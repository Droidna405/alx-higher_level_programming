# 0x0E. SQL - More queries

## Resources

Read or watch:

How To Create a New User and Grant Permissions in MySQL<https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql>
How To Use MySQL GRANT Statement To Grant Privileges To a User<https://www.mysqltutorial.org/mysql-administration/mysql-grant/>
MySQL constraints<https://zetcode.com/mysql/constraints/>
SQL technique: subqueries
Basic query operation: the join
SQL technique: multiple joins and the distinct keyword
SQL technique: join types
SQL technique: union and minus
MySQL Cheat Sheet
The Seven Types of SQL Joins
MySQL Tutorial
SQL Style Guide
MySQL 8.0 SQL Statement Syntax

## General

    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What’s a PRIMARY KEY
    What’s a FOREIGN KEY
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What are subqueries
    What are JOIN and UNION

## More Info
Comments for your SQL file:

$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

## Install MySQL 8.0 on Ubuntu 20.04 LTS

$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$


By Joel Mwangala <joemwangala@gmail.com>
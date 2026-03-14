# Python MySQL Database Application with Tkinter

## Project Overview

This project demonstrates how to build a **Python application connected to a MySQL database** and display data using a **Tkinter graphical interface**.

The system manages three main entities:

* Users
* Profiles
* Posts

This project is designed for **learning and teaching purposes**. It helps students understand how to:

* Design a relational database
* Write SQL queries
* Connect Python to MySQL
* Perform CRUD operations
* Use SQL JOIN queries
* Build a simple GUI interface with Tkinter

---

# System Architecture

```
MySQL Database
      ↓
configuration.py
(Database Connection)
      ↓
users.py / profiles.py / posts.py
(Database Operations)
      ↓
interface.py
(Graphical User Interface)
```

---

# Project Structure

```
project_folder
│
├── configuration.py
├── users.py
├── profiles.py
├── posts.py
├── users_profiles_posts.py
├── interface.py
└── README.md
```

## File Descriptions

| File                    | Purpose                                |
| ----------------------- | -------------------------------------- |
| configuration.py        | Creates connection to MySQL database   |
| users.py                | Handles user operations                |
| profiles.py             | Handles profile operations             |
| posts.py                | Handles post operations                |
| users_profiles_posts.py | Demonstrates SQL JOIN queries          |
| interface.py            | Graphical interface built with Tkinter |

---

# Technologies Used

* Python 3
* MySQL
* mysql-connector-python
* Tkinter GUI

---

# Requirements

Make sure the following are installed:

* Python 3.x
* MySQL Server
* pip package manager

Install required Python library:

```
pip install mysql-connector-python
```

---

# Database Setup

Create the database:

```
CREATE DATABASE social_media;
USE social_media;
```

---

# Create Tables

## Users Table

```
CREATE TABLE users(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100)
);
```

Example data:

```
INSERT INTO users(name) VALUES
('John'),
('Alice'),
('David');
```

---

## Profiles Table

```
CREATE TABLE profiles(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
age INT,
city VARCHAR(100),
FOREIGN KEY(user_id) REFERENCES users(id)
);
```

Example data:

```
INSERT INTO profiles(user_id,age,city) VALUES
(1,23,'Kigali'),
(2,30,'Nairobi'),
(3,28,'Kampala');
```

---

## Posts Table

```
CREATE TABLE posts(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT,
text TEXT,
likes INT,
FOREIGN KEY(user_id) REFERENCES users(id)
);
```

Example data:

```
INSERT INTO posts(user_id,text,likes) VALUES
(1,'Hello World',10),
(2,'Learning MySQL',7),
(3,'Python is great',5);
```

---

# Python Database Connection

File: **configuration.py**

```
import mysql.connector

def get_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="social_media",
        port=3306
    )

    print("Database Connected")
    return conn
```

Update the credentials according to your MySQL setup.

---

# Reading Users from Database

File: **users.py**

```
from configuration import get_db

def read_users():
    conn = get_db()
    cursor = conn.cursor()

    query = "SELECT * FROM users"
    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        print(row)
```

---

# Insert New User

```
def insert_user(name):

    conn = get_db()
    cursor = conn.cursor()

    query = "INSERT INTO users (name) VALUES (%s)"

    cursor.execute(query,(name,))
    conn.commit()
```

---

# Update User

```
def update_user(user_id,new_name):

    conn = get_db()
    cursor = conn.cursor()

    query = "UPDATE users SET name=%s WHERE id=%s"

    cursor.execute(query,(new_name,user_id))
    conn.commit()
```

---

# Delete User

```
def delete_user(user_id):

    conn = get_db()
    cursor = conn.cursor()

    query = "DELETE FROM users WHERE id=%s"

    cursor.execute(query,(user_id,))
    conn.commit()
```

---

# Reading Profiles

File: **profiles.py**

```
SELECT * FROM profiles;
```

Example result:

```
id  user_id  age  city
1   1        23   Kigali
2   2        30   Nairobi
```

---

# Reading Posts

File: **posts.py**

```
SELECT * FROM posts;
```

Example result:

```
id  user_id  text            likes
1   1        Hello World     10
2   2        Learning MySQL  7
```

---

# SQL JOIN Example

File: **users_profiles_posts.py**

```
SELECT u.id, u.name, p.age, p.city, po.text, po.likes
FROM users u
JOIN profiles p ON u.id = p.user_id
JOIN posts po ON u.id = po.user_id;
```

Result:

```
id name  age city   text            likes
1  John  23  Kigali Hello World     10
2  Alice 30  Nairobi Learning MySQL 7
```

This query combines **multiple tables into one result**.

---

# Graphical Interface

File: **interface.py**

The interface uses Tkinter.

```
import tkinter as tk
from tkinter import ttk
```

Features of the GUI:

* Display database tables
* Navigate between tabs
* View users
* View profiles
* View posts

---

# Running the Application

Step 1 – Start MySQL server.

Step 2 – Create database and tables.

Step 3 – Update database credentials in:

```
configuration.py
```

Step 4 – Run the application:

```
python interface.py
```

The GUI will open and display the database information.

---

# Learning Objectives

Students will learn:

* Relational database design
* SQL queries
* Database normalization
* Python database connectivity
* CRUD operations
* SQL JOIN operations
* GUI development using Tkinter

---

# Practical Exercises for Students

## Exercise 1

Insert a new user.

Example:

```
Name: Peter
```

---

## Exercise 2

Add profile information:

```
Age: 25
City: Kigali
```

---

## Exercise 3

Create a post:

```
Text: Hello MySQL
Likes: 5
```

---

## Exercise 4

Run the JOIN query and analyze the results.

---

# Expected Learning Outcome

By the end of this project students should be able to:

* Create a MySQL database
* Design relational tables
* Connect Python to MySQL
* Write SQL queries
* Build simple data-driven applications

---

# Author:
#### Dr. ABINEZA Claudia

Educational project for learning:

* Python
* MySQL
* Database Applications

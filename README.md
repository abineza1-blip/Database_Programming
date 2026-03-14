# 📘 Database Programming Teaching Notes  
## From MySQL → Python → Graphical Interface (Tkinter)

---

## 1. Introduction to Databases 🗄️

A **database** is an organized collection of data stored electronically.

### Real-world examples

- School records system
- Hospital management system
- Banking system
- Social media platforms

---

## 2. MySQL Database 🐬

MySQL is a **Relational Database Management System (RDBMS)** used to store structured data in tables.

### Key Features

- Stores data in tables (rows and columns)
- Uses SQL (Structured Query Language)
- Fast and reliable
- Open-source
- Supports multi-user access

---

## 3. Core Database Concepts

### 3.1 Table

A table stores data in rows and columns.

Example: Users table

| id | name |
|----|------|
| 1  | Alice |
| 2  | John  |

---

### 3.2 Primary Key 🔑

A column that uniquely identifies each record.

```sql
id INT PRIMARY KEY

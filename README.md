# 📘 Database Programming with MySQL, Python, and Tkinter
## Complete Teaching Notes & Practical Guide

---

## 📌 Course Module Overview

This module introduces students to the development of database-driven applications using:

- Relational database concepts
- MySQL Database Management System
- SQL for data manipulation
- Python for database connectivity
- Graphical User Interface (GUI) development using Tkinter

By the end of this module, students will build a fully functional desktop application connected to a relational database.

---

## 🎯 Learning Objectives

After completing this module, students will be able to:

- Explain database fundamentals
- Design relational database schemas
- Create databases and tables in MySQL
- Write SQL queries (CRUD operations)
- Use SQL JOIN to combine data from multiple tables
- Connect Python applications to MySQL databases
- Develop database-driven applications
- Design graphical user interfaces using Tkinter
- Integrate GUI with backend database operations

---

## 🧠 1. Introduction to Databases

A **database** is an organized collection of data stored electronically for efficient access and management.

### Real-world examples

- Student Information System
- Hospital Management System
- Banking System
- E-commerce Platforms
- Social Media Applications

---

## 🗄️ 2. Relational Database Concept

A **Relational Database** stores data in tables that are related to each other.

### Key Characteristics

- Data stored in rows and columns
- Tables linked through keys
- Supports structured queries (SQL)
- Ensures data integrity and consistency

---

## 🐬 3. MySQL Database Management System

MySQL is a widely used Relational Database Management System (RDBMS).

### Features

- Open-source
- High performance
- Secure and reliable
- Multi-user support
- Cross-platform compatibility

---

## 🏗️ 4. Database Design Example: Social Media System

We will build a simple system with three tables:

- Users
- Profiles
- Posts

---

## 📋 5. Table Structures

### 5.1 Users Table

Stores basic user information.

```sql
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

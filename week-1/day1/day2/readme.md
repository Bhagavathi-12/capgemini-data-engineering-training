# 📊 SQL Joins & GROUP BY Assignment

## 📌 Overview
This project contains SQL concepts and practice questions covering:
- SQL Joins (INNER, LEFT, RIGHT, FULL)
- GROUP BY operations
- Real-world SQL scenarios

---

## 📂 Files in Project
- `Joins.docx` → SQL Join concepts + 30 questions
- `Assignment_3.docx` → GROUP BY + 30 questions
- `README.md` → Documentation

---

## 🔗 SQL JOINS

### INNER JOIN
Returns only matching records.

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
```

---

### LEFT JOIN
Returns all employees + matching departments.

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;
```

---

### RIGHT JOIN
Returns all departments + matching employees.

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
RIGHT JOIN departments d
ON e.dept_id = d.dept_id;
```

---

### FULL OUTER JOIN
Returns all records from both tables.

```sql
SELECT e.emp_name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d
ON e.dept_id = d.dept_id;
```

---

## 🧱 TABLE STRUCTURE

### Employees

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    manager_id INT,
    dept_id INT
);
```

---

### Departments

```sql
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);
```

---

### Projects

```sql
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    emp_id INT
);
```

---

## 📊 GROUP BY

### Employee Table

```sql
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);
```

---

### Sales Table

```sql
CREATE TABLE Sales (
    sales_id INT PRIMARY KEY,
    emp_id INT,
    product VARCHAR(50),
    amount DECIMAL(10,2),
    sale_date DATE
);
```

---

## 📈 GROUP BY Examples

### Total Salary

```sql
SELECT department, SUM(salary) AS total_salary
FROM Employee
GROUP BY department;
```

---

### Average Salary

```sql
SELECT department, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department;
```

---

### Employee Count

```sql
SELECT department, COUNT(*) AS total_employees
FROM Employee
GROUP BY department;
```

---

## 🧠 Topics Covered
- Joins (INNER, LEFT, RIGHT, FULL)
- NULL handling
- Aggregations (SUM, COUNT, AVG, MAX, MIN)
- GROUP BY + HAVING
- Joins with aggregation

---

## 📝 Practice

### Joins (30 Questions)
- Employee–Manager queries
- Employees without departments
- Projects mapping
- Departments without employees

### GROUP BY (30 Questions)
- Salary analysis
- Sales reports
- Employee performance

---

## 🚀 How to Run

1. Open VS Code
2. Install SQL extension (optional)
3. Copy SQL queries into your DB tool (MySQL / PostgreSQL)
4. Run queries step by step

---

## 🎯 Outcome
After completing this:
- You can write JOIN queries confidently
- You can use GROUP BY effectively
- You can solve real-world SQL problems

---

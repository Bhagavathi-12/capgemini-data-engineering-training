# 📊 SQL Practice Assignment (CASE WHEN + Window Functions)

## 📌 Overview
This project contains SQL practice problems focused on:
- CASE WHEN (basic & nested)
- Window Functions (ROW_NUMBER, RANK, DENSE_RANK)

It is designed for interview preparation and hands-on SQL learning.

---

## 📂 Project Files
- `Assignment_1.docx` → CASE WHEN Problems
- `WFunctions1.docx` → Window Functions Problems
- `README.md` → Documentation

---

# 🧱 DATABASE SETUP

## 1️⃣ Employee Table (CASE WHEN)

```sql
CREATE TABLE Employee (
emp_id INT,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
experience INT,
performance_rating CHAR(1)
);
```

---

## 2️⃣ Employee Table (Window Functions)

```sql
CREATE TABLE employees (
emp_id INT,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
join_date DATE
);
```

---

## ⚠️ Important Fix
❌ Wrong in file:
```sql
INSERT INTO orders VALUES ...
```

✅ Correct:
```sql
INSERT INTO employees VALUES ...
```

---

# 🔥 CASE WHEN PROBLEMS

## ✅ Salary Hike

```sql
SELECT *,
CASE 
    WHEN experience >= 8 AND performance_rating = 'A' THEN salary * 1.20
    WHEN experience >= 5 AND performance_rating = 'B' THEN salary * 1.15
    WHEN performance_rating = 'C' THEN salary
    ELSE salary * 1.10
END AS new_salary
FROM Employee;
```

---

## ✅ Bonus Calculation

```sql
SELECT *,
CASE 
    WHEN department = 'Finance' THEN 
        CASE 
            WHEN performance_rating = 'A' THEN salary * 0.20
            WHEN performance_rating = 'B' THEN salary * 0.15
            ELSE salary * 0.05
        END
    WHEN department = 'Engineering' THEN 
        CASE 
            WHEN performance_rating = 'A' THEN salary * 0.18
            WHEN performance_rating = 'B' THEN salary * 0.12
            ELSE salary * 0.03
        END
    ELSE salary * 0.10
END AS bonus
FROM Employee;
```

---

## ✅ Employee Categorization

```sql
SELECT *,
CASE 
    WHEN salary > 80000 AND performance_rating = 'A' THEN 'High Performer'
    WHEN salary BETWEEN 50000 AND 80000 AND performance_rating = 'B' THEN 'Mid Performer'
    ELSE 'Low Performer'
END AS category
FROM Employee;
```

---

## ✅ Risk Assessment

```sql
SELECT *,
CASE 
    WHEN department = 'HR' THEN 
        CASE 
            WHEN experience < 5 THEN 'High Risk'
            ELSE 'Low Risk'
        END
    WHEN department IN ('Engineering','Finance') THEN 
        CASE 
            WHEN experience > 8 THEN 'Low Risk'
            ELSE 'Medium Risk'
        END
    ELSE 'Medium Risk'
END AS risk_level
FROM Employee;
```

---

# 🚀 WINDOW FUNCTIONS

## 🔹 ROW_NUMBER()

```sql
SELECT *, ROW_NUMBER() OVER (ORDER BY salary DESC) rn FROM employees;
```

```sql
SELECT *, ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) rn FROM employees;
```

```sql
SELECT *, ROW_NUMBER() OVER (ORDER BY join_date DESC) rn FROM employees;
```

---

## 🔹 RANK()

```sql
SELECT *, RANK() OVER (ORDER BY salary DESC) rnk FROM employees;
```

```sql
SELECT *, RANK() OVER (PARTITION BY department ORDER BY salary DESC) rnk FROM employees;
```

---

## 🔹 DENSE_RANK()

```sql
SELECT *, DENSE_RANK() OVER (ORDER BY salary DESC) dr FROM employees;
```

```sql
SELECT *, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) dr FROM employees;
```

---

# 🧠 Concepts Covered

## CASE WHEN
- Conditional logic in SQL
- Nested CASE statements
- Real-world business rules

## Window Functions
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- PARTITION BY
- ORDER BY

---

# ⚡ How to Run in VS Code

1. Install SQLTools extension  
2. Connect to MySQL/PostgreSQL  
3. Copy table creation scripts  
4. Insert data  
5. Run queries step-by-step  

---

# 🎯 Learning Outcome

After completing this project, you will:
- Master CASE WHEN logic
- Understand ranking functions deeply
- Solve real interview-level SQL problems

---

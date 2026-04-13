# SQL REGEX Practice Assignment

## Overview
This project contains a SQL REGEX practice assignment designed to improve pattern matching and data extraction skills using SQL.

---

## Table Details

Table Name: regex_practice

Columns:
- id (INT)
- full_text (VARCHAR)
- email (VARCHAR)
- phone (VARCHAR)
- mixed_value (VARCHAR)

---

## Table Creation

CREATE TABLE regex_practice (
    id INT,
    full_text VARCHAR(200),
    email VARCHAR(100),
    phone VARCHAR(30),
    mixed_value VARCHAR(100)
);

---

## Data Description

- Contains 40 rows of sample data
- Includes:
  - Emails (gmail, yahoo, outlook, company domains)
  - Phone numbers (with and without country codes)
  - Mixed alphanumeric values
  - Structured text patterns

---

## Assignment Questions

1. Extract numbers at the beginning of mixed_value  
2. Extract numbers at the end of mixed_value  
3. Extract first character from mixed_value  
4. Extract last character from mixed_value  
5. Extract exactly two digits  
6. Extract exactly one digit  
7. Extract country code from phone  
8. Extract numbers between alphabets  
9. Extract text before @ in email  
10. Extract text after @ in email  
11. Extract domain name  
12. Extract text after last dot  
13. Extract alphabets only  
14. Extract numbers only  
15. Extract first 3 characters from full_text  
16. Extract last 2 characters from full_text  
17. Extract employee number  
18. Extract country code at end  
19. Extract text between underscores  
20. Extract country code after +  

---

## Skills Covered

- Regular Expressions (REGEX)
- String manipulation
- Pattern matching
- Data cleaning
- SQL querying

---

## Tools Used

- SQL (MySQL / PostgreSQL / Oracle / Spark SQL)
- VS Code
- Databricks (optional)

---

## How to Run

1. Create the table
2. Insert the dataset
3. Run REGEX queries
4. Validate results

---

## Learning Outcomes

- Understand REGEX patterns
- Extract data from complex strings
- Improve SQL problem-solving
- Prepare for interviews

---
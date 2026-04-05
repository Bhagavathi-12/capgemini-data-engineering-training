# 📊 Business Pipeline & Analytics (PySpark Mini Project)

## 📌 Overview
This project focuses on building an **end-to-end data pipeline using PySpark** to transform raw data into meaningful business insights. It demonstrates key data engineering concepts such as **data cleaning, transformation, aggregation, and reporting**.

The pipeline processes customer and sales data to generate analytics like revenue trends, customer segmentation, and top-performing customers.

---

## 🎯 Objective
To design a structured workflow that:
- Cleans raw data
- Performs business-level aggregations
- Generates actionable insights
- Produces a final reporting dataset

---

## ⚙️ Tech Stack
- PySpark
- Python
- CSV Data Sources

---

## 🧹 Data Cleaning Steps
Before processing, the dataset is cleaned to ensure accuracy:
- Remove rows with null keys (e.g., `customer_id`)
- Remove duplicate records
- Filter invalid values (e.g., negative sales amounts)
- Check and correct column data types

---

## 📈 Project Tasks

### 1. Daily Sales
- Calculate total sales per day  
- Output: `date, total_sales`

### 2. City-wise Revenue
- Aggregate revenue by city  
- Output: `city, total_revenue`

### 3. Top 5 Customers
- Identify highest spending customers  
- Output: `customer_name, total_spend`

### 4. Repeat Customers
- Find customers with more than one order  
- Output: `customer_id, order_count`

### 5. Customer Segmentation
Segment customers based on total spending:
- Gold → > 10000  
- Silver → 5000 – 10000  
- Bronze → < 5000  

Output: `customer_name, total_spend, segment`

### 6. Final Reporting Table
Combine all insights into one dataset:
- Output:  
  `customer_name, city, total_spend, order_count, segment`

### 7. Save Output
Final dataset is stored as CSV:

```python
final_df.write.mode('overwrite').csv('/samples/output/report')
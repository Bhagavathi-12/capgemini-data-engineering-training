# 🛒 Olist Data Engineering Pipeline using PySpark (Databricks)

## 📌 Project Overview
This project demonstrates an **end-to-end data engineering pipeline** using the **Olist Brazilian E-commerce Dataset** on Databricks. The pipeline involves data ingestion, transformation, analysis using PySpark, and building a final reporting dataset.

The goal is to apply real-world data engineering concepts such as **joins, aggregations, window functions, and customer segmentation**.

---

## 🎯 Objectives
- Work with a real-world multi-table dataset
- Perform data ingestion and validation
- Apply transformations using PySpark
- Use window functions for advanced analytics
- Build a final reporting dataset

---

## 📂 Dataset
- Source: Olist Brazilian E-commerce Dataset (Kaggle)
- Files used:
  - `olist_customers_dataset.csv`
  - `olist_orders_dataset.csv`
  - `olist_order_payments_dataset.csv`
  - `olist_order_items_dataset.csv`
  - `olist_products_dataset.csv`

📥 Dataset Link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## ⚙️ Tech Stack
- **Apache Spark (PySpark)**
- **Databricks Community Edition**
- **Python**

---

## 🚀 Project Workflow

### 🔹 Step 1: Data Ingestion
- Uploaded CSV files into Databricks (`/FileStore/olist/`)
- Loaded data using PySpark DataFrames

```python
customers = spark.read.csv("/FileStore/olist/olist_customers_dataset.csv", header=True, inferSchema=True)
# 🔹 Phase 3A – Data Quality & Cleaning Challenge (PySpark)

## 🔹 Objective

The objective of this phase is to work with intentionally messy data and apply data cleaning techniques before building a data pipeline. This helps in understanding the importance of data quality in real-world data engineering. 

---

## 🔹 Problem Summary

A dataset containing customer details was provided with multiple data quality issues such as:

* Null values
* Duplicate records
* Missing primary keys
* Invalid values (e.g., negative age)

The task was to clean the dataset and prepare it for further processing and analysis.

---

## 🔹 Dataset Used

The dataset was created directly in PySpark:

```python
data = [
(1, "Ravi", "Hyderabad", 25),
(2, None, "Chennai", 32),
(None, "Arun", "Hyderabad", 28),
(4, "Meena", None, 30),
(4, "Meena", None, 30),
(5, "John", "Bangalore", -5)
]

columns = ["customer_id", "name", "city", "age"]
```

---

## 🔹 Approach

1. Loaded the dataset into a PySpark DataFrame
2. Identified data issues:

   * Null values
   * Duplicate rows
   * Invalid age values
3. Performed data cleaning:

   * Removed rows with null primary keys
   * Filled missing values for `name` and `city`
   * Removed duplicate records
   * Filtered out invalid age values (age < 0)
4. Validated the cleaning process:

   * Compared row counts before and after cleaning
5. Performed aggregation:

   * Calculated number of customers per city

---

## 🔹 Key Transformations Used

* `filter()` → to remove null and invalid values
* `fillna()` → to handle missing data
* `dropDuplicates()` → to remove duplicate records
* `groupBy()` → to group data by city
* `agg()` / `count()` → to calculate customer counts

---

## 🔹 Aggregation Example

```python
from pyspark.sql.functions import count

df_clean.groupBy("city") \
        .agg(count("customer_id").alias("customer_count")) \
        .show()
```

---

## 🔹 Output / Results

* Cleaned dataset with valid and consistent records
* Aggregated data showing customer distribution by city
* Improved data reliability for downstream processing

---

## 🔹 Data Engineering Considerations

* Data cleaning is mandatory before any transformation
* Null values can distort aggregation results
* Duplicate records can lead to incorrect insights
* Validation ensures correctness of processed data

---

## 🔹 Challenges Faced

* Identifying all types of data inconsistencies
* Deciding how to handle missing values effectively
* Ensuring no important data is lost during cleaning

---

## 🔹 Key Learnings

* Real-world data is often messy and unstructured
* Data cleaning significantly impacts analysis results
* Validation is essential in every data pipeline
* Even small data issues can lead to major business errors 

---

## 🔹 Reflection

* Skipping data cleaning leads to incorrect insights
* Invalid values (like negative age) have high impact on results
* Poor data quality can lead to wrong business decisions
* A proper cleaning checklist is essential before processing

---

## 🔹 Files in this Repository

* `solution.py` → PySpark implementation
* `phase3a_data_quality_challenge.pdf` → Problem statement
* `README.md` → Project documentation

---

## 🔹 Conclusion

This phase highlights the importance of data quality in data engineering. Cleaning and validating data ensures accurate analytics and reliable business decisions.

---

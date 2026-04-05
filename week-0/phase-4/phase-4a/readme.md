# Phase 4A – Bucketing and Segmentation in PySpark

## Objective
The goal of this phase is to understand how continuous data can be converted into categories using bucketing and segmentation techniques in PySpark.

## Problem Summary
In this task, we worked with customer transaction data and focused on dividing continuous values (like total spend) into meaningful categories such as Gold, Silver, and Bronze.

The tasks included:
- Creating customer segments using different methods
- Grouping and analyzing segmented data
- Comparing different segmentation approaches
- Understanding when to use each method

## Approach

First, the datasets were loaded and joined to create a combined dataset containing customer and sales information.

Then, customer-level aggregation was performed to calculate:
- Total spending of each customer
- Number of orders per customer

After preparing the data, multiple segmentation techniques were applied:

1. Conditional Logic  
   Used simple rules to assign Gold, Silver, and Bronze categories based on total spend.

2. Quantile-Based Segmentation  
   Divided customers into equal groups (Low, Medium, High) based on data distribution.

3. Bucketizer  
   Used predefined ranges to assign customers into buckets.

4. Window-Based Ranking  
   Ranked customers using percent_rank and then categorized them.

Finally, results from all methods were compared.

## Key Transformations Used

- `withColumn()` → to create new columns  
- `when()` → to apply conditional segmentation  
- `groupBy()` → to group data  
- `count()` → to count customers in each segment  
- `approxQuantile()` → to calculate quantile values  
- `Bucketizer` → to create fixed buckets  
- `Window` + `percent_rank()` → to rank customers  

## Output / Results

The final outputs include customer-level segmentation using different techniques.

Each output contains:
- customer_id  
- customer_name  
- city  
- total_spend  
- order_count  
- segment column (varies by method)

Different segmentation columns created:
- segment (conditional)
- quantile_seg
- bucket_seg
- rank_seg

These outputs help compare how each method classifies customers.

## Comparison of Methods

- Conditional Logic  
  Simple and easy to understand but not flexible  

- Quantile Segmentation  
  Balanced groups based on data distribution  

- Bucketizer  
  Uses fixed ranges and is efficient for large datasets  

- Window Ranking  
  Provides relative position of each customer  

## Data Engineering Considerations

- Ensured correct joins to avoid duplication  
- Aggregated data before applying segmentation  
- Maintained consistent output format  
- Used appropriate methods depending on the scenario  

## Challenges Faced

- Understanding differences between segmentation techniques  
- Choosing proper thresholds for bucketizer  
- Interpreting quantile outputs  
- Applying window functions correctly  

## Learnings

- Learned how segmentation simplifies data analysis  
- Understood difference between business rules and data-driven methods  
- Gained hands-on experience with PySpark transformations  
- Learned how ranking helps in identifying top customers  

## Reflection

Segmentation helps in converting raw numerical data into meaningful categories, making it easier for businesses to make decisions.

Fixed thresholds may fail when data distribution changes, whereas quantile-based methods adapt to data.

In real-world projects, a combination of quantile analysis and business rules is often the most effective approach.
## Final Thoughts

This phase provided a strong understanding of how different segmentation techniques work and when to use them.  
It also highlighted how the same data can produce different insights depending on the method used.
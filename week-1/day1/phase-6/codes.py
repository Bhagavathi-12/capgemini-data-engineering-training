from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.getOrCreate()

customers_data = [
    (1, "John Doe", "john@example.com", "Hyderabad"),
    (2, "Alice ", "alice@example.com", "Chennai"),
    (3, None, "bob@example.com", "Bangalore"),        
    (4, "David", None, "Mumbai"),                    
    (5, "Eva", "eva@example.com", "Hyderabad"),
    (6, "Frank", "frank@example.com", "Delhi"),
]

customers = spark.createDataFrame(customers_data, ["customer_id", "name", "email", "city"])

orders_data = [
    (101, 1, "2024-01-01", 1000),
    (102, 2, "2024-01-02", 2000),
    (103, 3, "2024-01-03", -500),     # INVALID negative value
    (104, 99, "2024-01-04", 1500),    # INVALID FK (customer_id 99)
    (105, 1, "2024-01-05", None),     # NULL amount
    (106, 5, "2024-01-06", 3000),
    (107, 5, "2024-01-07", 3000),     # duplicate-like record
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "order_date", "amount"])

import pyspark.sql.functions as F

orders = orders.withColumn("order_date", F.to_date(F.col("order_date")))

import pyspark.sql.functions as F

# Remove nulls and clean customers
customers_clean = customers \
    .dropna(subset=["customer_id", "name", "email"]) \
    .withColumn("name", F.trim(F.col("name")))

# Clean orders
orders_clean = orders \
    .filter(F.col("amount").isNotNull()) \
    .filter(F.col("amount") >= 0) \
    .dropDuplicates()

invalid_orders = orders_clean.join(
    customers_clean,
    on="customer_id",
    how="left_anti"
)

invalid_orders.show()

joined_df = orders_clean.join(
    customers_clean,
    on="customer_id",
    how="inner"
)

import pyspark.sql.functions as F

agg_df = joined_df.groupBy("customer_id", "name") \
    .agg(
        F.sum("amount").alias("total_spend"),
        F.count("order_id").alias("order_count")
    )

import pyspark.sql.functions as F
from pyspark.sql.window import Window

window_spec = Window.orderBy(F.col("total_spend").desc())

final_df = agg_df.withColumn(
    "rank",
    F.rank().over(window_spec)
)

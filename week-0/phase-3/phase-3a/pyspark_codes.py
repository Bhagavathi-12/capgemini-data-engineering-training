from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

data = [
(1, "Ravi", "Hyderabad", 25),
(2, None, "Chennai", 32),
(None, "Arun", "Hyderabad", 28),
(4, "Meena", None, 30),
(4, "Meena", None, 30),
(5, "John", "Bangalore", -5)
]

columns = ["customer_id", "name", "city", "age"]

df = spark.createDataFrame(data, columns)
df_clean = df.filter(col("customer_id").isNotNull())
df_clean = df_clean.fillna({
    "name": "Unknown",
    "city": "Unknown"
})
df_clean = df_clean.dropDuplicates()
df_clean = df_clean.filter(col("age") > 0)
print("Before Cleaning:", df.count())
print("After Cleaning:", df_clean.count())
from pyspark.sql.functions import count

df_clean.groupBy("city") \
        .agg(count("customer_id").alias("customer_count")) \
        .show()
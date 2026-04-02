from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("Phase3_ETL").getOrCreate()
customers = spark.read.option("header", "true").csv("/samples/customers.csv")
sales = spark.read.option("header", "true").csv("/samples/sales.csv")
customers.show()
sales.show()
customers.printSchema()
sales.printSchema()
#convert datatype
customers = customers.withColumn("customer_id", col("customer_id").cast("int"))

sales = sales.withColumn("customer_id", col("customer_id").cast("int")) \
             .withColumn("total_amount", col("total_amount").cast("double"))
#Remove nulls
customers_clean = customers.dropna()
sales_clean = sales.dropna()
#filter invalid records
sales_clean = sales_clean.filter(col("total_amount") > 0)
#Daily sales caluculation
daily_sales = sales_clean.groupBy("sale_date") \
    .agg(sum("total_amount").alias("daily_sales"))

daily_sales.show()
#city-wise revenue
customer_sales = sales_clean.join(customers_clean, "customer_id")

city_revenue = customer_sales.groupBy("city") \
    .agg(sum("total_amount").alias("total_revenue"))

city_revenue.show()
#Repeat customers
repeat_customers = sales_clean.groupBy("customer_id") \
    .agg(count("*").alias("order_count")) \
    .filter(col("order_count") > 2)

repeat_customers.show()
#Highest spending customer per city
customer_spend = customer_sales.groupBy("customer_id", "city") \
    .agg(sum("total_amount").alias("total_spend"))

window_spec = Window.partitionBy("city").orderBy(col("total_spend").desc())

top_customers = customer_spend.withColumn("rank", row_number().over(window_spec)) \
    .filter(col("rank") == 1)

top_customers.show()
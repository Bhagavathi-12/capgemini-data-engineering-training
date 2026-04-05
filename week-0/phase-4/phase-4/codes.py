from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("phase4").getOrCreate()

customers = spark.read.format('csv').option('header', 'true').load('/samples/customers.csv')
sales = spark.read.format('csv').option('header', 'true').load('/samples/sales.csv')
sales.show()
customers.show()

# Data Cleaning 
# remove nulls
customers = customers.dropna(subset=["customer_id"])
sales = sales.dropna(subset=["sale_id", "customer_id"])

# remove duplicates
customers = customers.dropDuplicates()
sales = sales.dropDuplicates()

# remove invalid values
sales = sales.filter(col("total_amount")>0)

# tasks
# task1 - daily sales
daily_sales = sales.groupBy(col("sale_date").alias("date")).agg(sum("total_amount").alias("total_sales"))
daily_sales.show()

# task2 - city-wise revenue
city_revenue = customers.join(sales, "customer_id").groupBy("city").agg(sum("total_amount").alias("total_revenue"))
city_revenue.show()

# task3 - top 5 customers
# here we need cuatomers sales table joined and we need a column called customer_name so we join first_name last_name below
cs_joined = customers.join(sales, "customer_id")
cs_joined= cs_joined.withColumn("customer_name", concat_ws(" ", "first_name", "last_name"))
top_customers = cs_joined.groupBy("customer_name").agg(sum("total_amount").alias("total_spend")).orderBy("total_spend").limit(5)
top_customers.show()

# task4 - repeat customers(>1 order)
repeat_customers = customers.join(sales, "customer_id").groupBy("customer_id").agg(count("sale_id").alias("order_count")).filter(col("order_count")>1)
repeat_customers.show()

# task5 - customer segmentation - Create business logic: total_spend > 10000 → Gold 5000–10000 → Silver <5000 → Bronze Output: customer_name, total_spend, segment
customer_spends = cs_joined.groupBy("customer_name").agg(sum("total_amount").alias("total_spend"))
segmented_customers = customer_spends.withColumn("segment", when(col("total_spend") > 100, "Gold").when((col("total_spend") >= 50) & (col("total_spend") <= 100), "Silver").otherwise("Bronze"))
segmented_customers.show()

# task6 - final Reporting Table: Combine all relevant insights into a final table. Output should include:customer_name, city, total_spend, order_count, segment
final_report = cs_joined.groupBy("customer_id", "customer_name", "city") \
  .agg(sum("total_amount").alias("total_spend"), 
       count("sale_id").alias("order_count")
      )
final_report = final_report.withColumn(
  "segment", 
  when(col("total_spend") >100 , "Gold")
  .when((col("total_spend") >= 50) & (col("total_spend") <=100) , "Silver") 
  .otherwise("Bronze")
       )

final_report.show();

# Save Output → final_df.write.mode('overwrite').csv('/samples/output/report' Since samples folder is read only here I written it in tmp
final_report.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("/tmp/output/report")
                                       
from pyspark.sql.functions import *
from pyspark.sql.window import Window
print('Setup complete')


display(dbutils.fs.ls('/Volumes/olist/data/volume'))

orders = spark.read.csv('/Volumes/olist/data/volume/olist_orders_dataset.csv', header=True, inferSchema=True)
order_items = spark.read.csv('/Volumes/olist/data/volume/olist_order_items_dataset.csv', header=True, inferSchema=True)
customers = spark.read.csv('/Volumes/olist/data/volume/olist_customers_dataset.csv', header=True, inferSchema=True)
products = spark.read.csv('/Volumes/olist/data/volume/olist_products_dataset.csv', header=True, inferSchema=True)
payments = spark.read.csv('/Volumes/olist/data/volume/olist_order_payments_dataset.csv', header=True, inferSchema=True)

display(orders)
display(customers)
display(order_items)
orders.printSchema()

orders.select([count(when(col(c).isNull(), c)).alias(c) for c in orders.columns]).show()
print('Orders:', orders.count())
print('Customers:', customers.count())

orders_customers = orders.join(customers, 'customer_id', 'inner')
display(orders_customers)

#Top3 customers
df = customers.join(orders, "customer_id") \
              .join(payments, "order_id")

customer_spend = df.groupBy("customer_id", "customer_city") \
    .agg(sum("payment_value").alias("total_spend"))

window_spec = Window.partitionBy("customer_city").orderBy(col("total_spend").desc())

top3 = customer_spend.withColumn("rank", row_number().over(window_spec)) \
    .filter(col("rank") <= 3)

display(top3)

#Running Total sales
df = orders.join(payments, "order_id")

daily_sales = df.groupBy(to_date("order_purchase_timestamp").alias("date")) \
    .agg(sum("payment_value").alias("daily_sales"))

window_spec = Window.orderBy("date")

running_total = daily_sales.withColumn("running_total", sum("daily_sales").over(window_spec))

display(running_total)

#Customer lifetimr value
df = customers.join(orders, "customer_id") \
              .join(payments, "order_id")

clv = df.groupBy("customer_id") \
    .agg(sum("payment_value").alias("total_spend"))

display(clv)

#Customer segmentation
segmented = clv.withColumn(
    "segment",
    when(col("total_spend") > 10000, "Gold")
    .when((col("total_spend") >= 5000) & (col("total_spend") <= 10000), "Silver")
    .otherwise("Bronze")
)

segment_count = segmented.groupBy("segment").count()

display(segmented)
display(segment_count)

#Final reporting table
total_orders = orders.groupBy("customer_id") \
    .agg(count("order_id").alias("total_orders"))

final_df = segmented.join(customers, "customer_id") \
    .join(total_orders, "customer_id") \
    .select(
        "customer_id",
        "customer_city",
        "total_spend",
        "segment",
        "total_orders"
    )

display(final_df)
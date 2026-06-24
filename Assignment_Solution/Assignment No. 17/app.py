from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Sales Data Analysis").getOrCreate()

df = spark.read.csv(
    "data/sales.csv",
    header=True,
    inferSchema=True
)

print("Products Sorted by Sales (Descending)")

sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("Top 3 Products by Sales")

top3_df = sorted_df.limit(3)
top3_df.show()

print("Products with Sales > 80000")

filtered_df = df.filter(col("sales") > 80000)
filtered_df.show()

filtered_df.coalesce(1).write.mode("overwrite").option("header", True).csv("output/high_sales_products")

print("Filtered data saved successfully.")

spark.stop()
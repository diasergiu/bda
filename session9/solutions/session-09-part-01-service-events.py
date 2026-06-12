from pyspark.sql import SparkSession
from pyspark.sql.types import (
    DoubleType,
    IntegerType,
    StringType,
    StructField,
    StructType,
    TimestampType,
)

events_path = "datasets/service_events.csv"

spark = (
    SparkSession.builder
    .appName("Session09Part01")
    .master("local[*]")
    .getOrCreate()
)

schema = StructType([
    StructField("event_id", IntegerType(), True),
    StructField("service", StringType(), True),
    StructField("region", StringType(), True),
    StructField("event_time", TimestampType(), True),
    StructField("request_count", IntegerType(), True),
    StructField("error_count", IntegerType(), True),
    StructField("latency_ms", DoubleType(), True),
    StructField("bytes_in", DoubleType(), True),
    StructField("bytes_out", DoubleType(), True),
])

events_df = (
    spark.read
    .option("header", True)
    .schema(schema)
    .csv(events_path)
)


# events_df.printSchema()
# events_df.show(5, truncate=False)

# print("Rows:", events_df.count())
# print("Columns:", events_df.columns)


events_df.createOrReplaceTempView("service_events")

# spark.sql("""
#     SELECT service, region, event_time, request_count
#     FROM service_events
#     ORDER BY event_time
#     LIMIT 10
# """).show(truncate=False)
print("---------------------------------------- ")
# how many data are in the view
spark.sql("""
    Select count(*) as total 
          from service_events
    """).show()
print("---------------------------------------- ")

# how many services are in the view
spark.sql("""
          Select Distinct(service) as services
          from service_events
          """).show()
print("---------------------------------------- ")
# how many rows each region has
spark.sql("""
    SELECT region, COUNT(*) as total
    FROM service_events
    GROUP BY region
    """).show()

spark.stop()
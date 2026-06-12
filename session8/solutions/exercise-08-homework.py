import os
import sys

os.environ.setdefault("PYSPARK_PYTHON", sys.executable)

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg


spark = (
    SparkSession.builder
    .appName("Session08LocalCheck")
    .master("local[*]")
    .getOrCreate()
)

dataOnlineOrder = [
    ()
]

df = spark.createDataFrame(dataOnlineOrder, ["city", "category", "revenue"])

df.show()



spark.stop()
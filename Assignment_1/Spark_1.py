# import findspark 
# findspark.init()
from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Spark Test") \
    .getOrCreate()

# Test DataFrame creation
data = [(1, "Alice"), (2, "Bob")]
columns = ["ID", "Name"]

df = spark.createDataFrame(data, columns)
df.show()

# Stop SparkSession
spark.stop()

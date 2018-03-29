from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, col, lit
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    parking_path = sys.argv[1]

    spark = SparkSession \
    .builder \
    .appName("Python Spark SQL for assignment 2") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    parking = spark.read.format('csv').options(header='true',inferschema='true').load(parking_path)
    parking.createOrReplaceTempView("parking")

    results = spark.sql("select violation_code, count(*) as cnt from parking group by violation_code")

    results.select(concat(col("violation_code"), lit("\t"), col("cnt")).alias("final")) \
            .write.save("task2-sql.out",format="text")
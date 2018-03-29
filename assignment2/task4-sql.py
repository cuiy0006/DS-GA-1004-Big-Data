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

    results = spark.sql("(select registration_state, count(*) as cnt from parking where registration_state = 'NY' group by registration_state) union (select 'Other' as registration_state, count(*) as cnt from parking where registration_state != 'NY')")

    results.select(concat(col("registration_state"), lit("\t"), col("cnt")).alias("final")) \
            .write.save("task4-sql.out",format="text")
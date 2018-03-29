from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, col, lit
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    open_path = sys.argv[1]

    spark = SparkSession \
    .builder \
    .appName("Python Spark SQL for assignment 2") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    open = spark.read.format('csv').options(header='true',inferschema='true').load(open_path)
    open.createOrReplaceTempView("open")

    results = spark.sql("select license_type, CAST(sum(amount_due) AS DECIMAL(16,2)) as total, CAST(sum(amount_due)/count(*) AS DECIMAL(16,2)) as average from open group by license_type")
    results.select(concat(col("license_type"), lit("\t"), col("total"), lit(", "), col("average")).alias("final")) \
            .write.save("task3-sql.out",format="text")
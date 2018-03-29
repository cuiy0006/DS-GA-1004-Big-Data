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

    tmp = spark.sql('select plate_id, registration_state, count(*) as cnt from parking group by plate_id, registration_state')
    tmp.createOrReplaceTempView('tmp')

    results = spark.sql('select plate_id, registration_state, cnt from tmp where cnt = (select max(cnt) from tmp)')

    results.select(concat(col("plate_id"), lit(", "), col("registration_state"), lit("\t"), col("cnt")).alias("final")) \
            .write.save("task5-sql.out",format="text")
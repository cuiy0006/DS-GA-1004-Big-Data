from pyspark.sql import SparkSession
from pyspark.sql.functions import concat, col, lit
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    parking_path = sys.argv[1]
    open_path = sys.argv[2]

    spark = SparkSession \
    .builder \
    .appName("Python Spark SQL for assignment 2") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    open = spark.read.format('csv').options(header='true',inferschema='true').load(open_path)
    parking = spark.read.format('csv').options(header='true',inferschema='true').load(parking_path)

    open.createOrReplaceTempView("open")
    parking.createOrReplaceTempView("parking")
    tmp = spark.sql("select P.summons_number, P.plate_id, P.violation_precinct, P.violation_code, P.issue_date, O.summons_number as dummy from parking P left join open O on P.summons_number = O.summons_number")
    tmp.createOrReplaceTempView('tmp')
    results = spark.sql('select summons_number, plate_id, violation_precinct, violation_code, date_format(issue_date, "yyyy-MM-dd") as issue_date from tmp where dummy is NULL')

    results.select(concat(col("summons_number"), lit("\t"), col("plate_id"), lit(", "), col("violation_precinct"), lit(", "), col("violation_code"), lit(", "), col("issue_date")).alias("final")) \
            .write.save("task1-sql.out",format="text")
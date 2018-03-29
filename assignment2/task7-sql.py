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

    parking_unique = spark.sql("select violation_code from parking group by violation_code")
    parking_unique.createOrReplaceTempView("parking_unique")

    weekday_tmp = spark.sql("select violation_code, CAST(count(*)/23 AS DECIMAL(16,2)) weekday_average, 0.00 weekend_average from parking where date_format(issue_date, 'EEEE') != 'Sunday' and date_format(issue_date, 'EEEE') != 'Saturday' group by violation_code")
    weekend_tmp = spark.sql("select violation_code, 0.00 weekday_average, CAST(count(*)/8 AS DECIMAL(16,2)) weekend_average from parking where date_format(issue_date, 'EEEE') = 'Sunday' or date_format(issue_date, 'EEEE') = 'Saturday' group by violation_code")
    weekday_tmp.createOrReplaceTempView('weekday_tmp')
    weekend_tmp.createOrReplaceTempView('weekend_tmp')


    results = spark.sql("select P.violation_code, (ifnull(E.weekend_average, 0.00) + ifnull(D.weekend_average, 0.00)) weekend_average , (ifnull(E.weekday_average, 0.00) + ifnull(D.weekday_average, 0.00)) weekday_average from parking_unique P left join weekday_tmp D on P.violation_code = D.violation_code left join weekend_tmp E on E.violation_code = P.violation_code")

    results.select(concat(col("violation_code"), lit("\t"), col("weekend_average"), lit(", "), col("weekday_average")).alias("final")) \
            .write.save("task7-sql.out",format="text")
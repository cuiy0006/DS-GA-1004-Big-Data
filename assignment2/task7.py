import sys
from pyspark import SparkContext
from csv import reader

weekends = set(['05', '06', '12', '13', '19', '20', '26', '27'])
NOofWeekend = 8
NOofWeekday = 23

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()

    parking_path = sys.argv[1]

    parking_lines = sc.textFile(parking_path, 1) \
                    .mapPartitions(lambda x:reader(x)) \
                    .map(lambda line: (line[2], (1, 0) if line[1].split('-')[2] not in weekends else (0, 1)))
    #(1, 0) today is weekday, (0, 1) today is weekend

    results = parking_lines.reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1])) \
            .map(lambda x: '{0:s}\t{1:.2f}, {2:.2f}'.format(x[0], float(x[1][1])/NOofWeekend, float(x[1][0])/NOofWeekday))

    results.saveAsTextFile('task7.out')
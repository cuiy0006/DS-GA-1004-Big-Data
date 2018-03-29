import sys
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    parking_path = sys.argv[1]
    sc = SparkContext()

    parking_lines = sc.textFile(parking_path, 1) \
                    .mapPartitions(lambda x:reader(x)) \
                    .map(lambda line: ((line[14], line[16]), 1))


    tmp = parking_lines.reduceByKey(lambda x,y: x + y).reduce(lambda x, y: x if x[1] > y[1] else y)
    results = sc.parallelize([tmp]) \
            .map(lambda x: '{0:s}, {1:s}\t{2:d}'.format(x[0][0], x[0][1], x[1]))

    results.saveAsTextFile('task5.out')
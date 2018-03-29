import sys
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    open_path = sys.argv[1]
    sc = SparkContext()

    open_lines = sc.textFile(open_path, 1) \
                    .mapPartitions(lambda x:reader(x)) \
                    .map(lambda line: (line[2], (float(line[12]), 1)))

    results = open_lines.reduceByKey(lambda x,y: (x[0] + y[0], x[1] + y[1])) \
            .map(lambda x: '{0:s}\t{1:.2f}, {2:.2f}'.format(x[0], x[1][0], x[1][0]/x[1][1]))

    results.saveAsTextFile('task3.out')
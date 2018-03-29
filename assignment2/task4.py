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
                    .map(lambda line: ('NY' if line[16] == 'NY' else 'Other', 1))


    results = parking_lines.reduceByKey(lambda x,y: x + y) \
            .map(lambda x: '{0:s}\t{1:d}'.format(x[0], x[1]))

    results.saveAsTextFile('task4.out')
import sys
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)

    parking_path = sys.argv[1]
    open_path = sys.argv[2]
    sc = SparkContext()

    open_lines = sc.textFile(open_path, 1) \
                .mapPartitions(lambda x:reader(x)) \
                .map(lambda line: (line[0], ('0',)))


    parking_lines = sc.textFile(parking_path, 1) \
                    .mapPartitions(lambda x:reader(x)) \
                    .map(lambda line: (line[0], ('1', line[14], line[6], line[2], line[1])))


    results = parking_lines.union(open_lines).reduceByKey(lambda x,y: reduceByKey_func(x,y)).filter(lambda z: z[1][0] != '0') \
            .map(lambda x: '{0:s}\t{1:s}, {2:s}, {3:s}, {4:s}'.format(x[0], x[1][1], x[1][2], x[1][3], x[1][4]))

    results.saveAsTextFile('task1.out')

def reduceByKey_func(x, y):
    if x[0] == '0' or y[0] == '0':
        return ('0',)
    else:
        return x

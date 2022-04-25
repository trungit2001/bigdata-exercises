from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('Lab8PySparkRDD')\
    .getOrCreate()

sc = spark.sparkContext

def pprint(rdd):
    for k, v in rdd.collect():
        print(f'{k}\t{v}')

rdd1 = sc.textFile('data.txt')
rdd2 = rdd1.flatMap(lambda x: x.split())
rdd3 = rdd2.map(lambda x: (x, 1))
rdd4 = rdd3.reduceByKey(lambda x, y: x + y)\
    .sortByKey()

pprint(rdd4)
from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('Lab8PySparkRDD')\
    .getOrCreate()

sc = spark.sparkContext

def pprint(rdd):
    for k, v in rdd.collect():
        print(f'{k}\t{v}')

rdd1 = sc.textFile('device.csv')
header = rdd1.first()

rdd2 = rdd1.filter(lambda row: row != header)
rdd3 = rdd2.map(
    lambda row: (
        row.split(',')[0], 
        (float(row.split(',')[1]), float(row.split(',')[1]))
    )
)
rdd4 = rdd3.reduceByKey(
    lambda x, y: (
        min(x[0], y[0]), 
        max(x[1], y[1])
    )
).sortByKey()

spark.createDataFrame(
    data=rdd4, 
    schema=['deviceID', 'min - max']
).show()
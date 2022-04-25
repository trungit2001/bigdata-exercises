from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('Lab8PySparkRDD')\
    .getOrCreate()

sc = spark.sparkContext

rdd1 = sc.textFile('device.csv')
header = rdd1.first()

rdd2 = rdd1.filter(lambda row: row != header)
rdd3 = rdd2.map(lambda row: (row.split(',')[0], 1))
rdd4 = rdd3.reduceByKey(lambda x, y: x + y).sortByKey()

spark.createDataFrame(
    data=rdd4, 
    schema=['deviceID', 'count']
).show()
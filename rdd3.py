from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('Lab8PySparkRDD')\
    .getOrCreate()
    
sc = spark.sparkContext

rdd1 = sc.textFile('hdfs://localhost:9000/input/device.csv')
header = rdd1.first()

rdd2 = rdd1.filter(lambda row: row != header)
rdd3 = rdd2.map(lambda row: row.split(','))
print(rdd3.collect())
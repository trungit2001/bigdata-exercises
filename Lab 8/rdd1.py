from pyspark.sql import SparkSession

spark = SparkSession \
    .builder\
    .appName('Lab8PySparkRDD')\
    .getOrCreate()
    
sc = spark.sparkContext

deviceID = ['1', '2', '6', '2', '3', '5', '4', '1', '2', '3', '7']
x = [0.1, 0.5, 0.2, 0.7, 0.8, 0.1, 0.3, 0.2, 0.4, 0.3, 0.7]

rdd1 = sc.parallelize(zip(deviceID, x))
print(rdd1.collect())
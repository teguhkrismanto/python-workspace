from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, trim
from main.base import PySparkJobInterface


class PySparkJob(PySparkJobInterface):

    def init_spark_session(self) -> SparkSession:
        spark = SparkSession.builder \
            .appName("Practice Test") \
            .getOrCreate()
        return spark

    def distinct_ids(self, data_file1: DataFrame) -> int:
        # TODO: Put your code here
        return data_file1.select("id").distinct().count()

    def valid_age_count(self, data_file2: DataFrame) -> int:
        # TODO: Put your code here
        return data_file2.withColumn("age", trim(col("age")).cast("int")) \
                     .filter((col("age").isNotNull()) & (col("age") >= 18)) \
                     .count()

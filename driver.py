from pyspark.sql import SparkSession
import sys

from src.main.workflows.workflow import initiate_workflow

spark = SparkSession.builder \
    .appName("DockerPySparkExample") \
    .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.0") \
    .getOrCreate()

if __name__ == '__main__':
    # perform_operation/configs can also be passed as argument due to time constraint skipping this part
    perform_operation = 'generate_and_anonymize'
    initiate_workflow(spark, perform_operation)

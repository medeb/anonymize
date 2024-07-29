import json

from faker import Faker
from pyspark import RDD
from pyspark.sql import functions as spark_functions, DataFrame


class PrepareData:
    def __init__(self, spark_session, number_of_records, columns):
        self.columns = columns
        self.spark_session = spark_session
        self.number_of_records = number_of_records

    def prepare(self):
        data = []
        fake = Faker()
        for _ in range(self.number_of_records):
            # can be extended keeping it simple for this
            data.append({
                self.columns[0]: fake.first_name(),
                self.columns[1]: fake.last_name(),
                self.columns[2]: fake.address().replace('\n', ', '),
                self.columns[3]: fake.date_of_birth().strftime("%Y-%m-%d")
            })

        sc = self.spark_session.sparkContext
        rdd: RDD = sc.parallelize(data)
        df: DataFrame = self.spark_session.createDataFrame(rdd)
        df.show(10, False)
        return df

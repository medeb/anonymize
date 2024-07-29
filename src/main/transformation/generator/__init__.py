from typing import List

from pyspark.sql import DataFrame, SparkSession

from src.main.transformation import BaseTransformation
from src.main.transformation.generator.prepare_data import PrepareData


class GenerateData(BaseTransformation):
    def __init__(self, spark_session, config):
        self.spark_session: SparkSession = spark_session
        self.columns: List[str] = config.get('columns')
        self.sink_path: str = config.get('sink_path')
        self.number_of_records: int = config.get('number_of_records')

    def apply(self):
        df = PrepareData(self.spark_session, self.number_of_records, self.columns).prepare()
        print(self.sink_path)
        df.write.mode('overwrite').csv(self.sink_path, header=True)
        df.show(2)
        return True

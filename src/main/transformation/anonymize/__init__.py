from pyspark.sql import DataFrame, SparkSession

from src.main.transformation.anonymize.parser import AnonParser
from src.main.transformation import BaseTransformation


class AnonymizeData(BaseTransformation):
    def __init__(self, spark_session, config):
        self.read_path = config.get('read_path')
        self.sink_path = config.get('sink_path')
        self.anonymizer_config = config.get('anonymizer_config', [{}])
        self.spark_session: SparkSession = spark_session

    def apply(self):
        df = self.spark_session.read.csv(self.read_path, header=True)
        df_parsed = AnonParser(df, self.anonymizer_config).parse()
        df_parsed.write.mode('overwrite').csv(self.sink_path, header=True)
        return True

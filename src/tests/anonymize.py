# tests/test_transformations.py
import json
import unittest
from pyspark.sql import SparkSession, DataFrame

from src.main.transformation.anonymize import AnonParser


def check_values_equal(value1, value2):
    return value1 == value2


class TestTransformations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder.master("local").appName("TestTransformations").getOrCreate()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

    def test_anonymize_transformation(self):
        # Sample data
        data = [
            (
                "1366 Harris Avenue Suite 514, Conradtown, MN 46888", "1943-10-07", "Daniel", "Young"
            )
        ]
        expected_result = {"address": "1366 Harris Avenue Suite 514, Conradtown, MN 46888",
                           "date_of_birth": "1943-10-07",
                           "first_name": "7297db81c2f7916e25b9593f8c8785e1aa1487fa9f3961c50b7cc5f1a541bc82",
                           "last_name": "****"}

        columns = ["address", "date_of_birth", 'first_name', "last_name"]
        anonymizer_config = [
            {
                "method": "sha256",
                "parameters": {
                    "column_name": "first_name"
                }
            },
            {
                "method": "replace",
                "parameters": {
                    "column_name": "last_name",
                    "replace_to": "****"
                }
            },
            {
                "method": "replace_with_regex",
                "parameters": {
                    "column_name": "address",
                    "replace_from_regex": "R\d",
                    "replace_to": "*"
                }
            }
        ]

        df = self.spark.createDataFrame(data, columns)
        df_parsed: DataFrame = AnonParser(df, anonymizer_config).parse()
        generated_result = json.loads(df_parsed.toJSON().collect()[0])
        for key, value in generated_result.items():
            self.assertTrue(check_values_equal(value, expected_result[key]))


if __name__ == '__main__':
    unittest.main()

from pyspark.sql import functions as spark_functions


class AnonParser:
    def __init__(self, df, user_defined_anon):
        self.df = df
        self.spark_functions = spark_functions
        self.user_defined_anon = user_defined_anon
        print(self.user_defined_anon)
        self.functions_map = {
            "replace": self.anon_replace,
            "replace_with_regex": self.anon_replace_with_regex,
            "sha256": self.anon_sha256,
        }

    def anon_replace(self, column_name, replace_to):
        self.df = self.df.withColumn(
            column_name, self.spark_functions.lit(replace_to))

    def anon_replace_with_regex(self, column_name, replace_from_regex, replace_to):
        self.df = self.df.withColumn(
            column_name, self.spark_functions.regexp_replace(column_name, replace_from_regex, replace_to))

    def anon_sha256(self, column_name):
        self.df = self.df.withColumn(
            column_name, self.spark_functions.sha2(self.df[column_name].cast('String'), 256))

    def parse(self):
        for current_check in self.user_defined_anon:
            current_name = current_check.get('method')
            current_parameters = current_check.get('parameters')
            self.functions_map[current_name](**current_parameters)
        return self.df

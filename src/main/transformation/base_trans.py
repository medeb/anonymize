from abc import ABC, abstractmethod
from pyspark.sql import DataFrame


class BaseTransformation(ABC):
    @abstractmethod
    def apply(self, df: DataFrame) -> DataFrame:
        pass

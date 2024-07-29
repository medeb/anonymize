from src.main.transformation import BaseTransformation, AnonymizeData, GenerateData


class TransformationFactory:
    @staticmethod
    def create_transformation(spark, transformation_type: str, **kwargs) -> BaseTransformation:
        print("Factory class called")
        if transformation_type == "data_generation":
            return GenerateData(spark, kwargs["config"])
        elif transformation_type == "data_anonymize":
            return AnonymizeData(spark, kwargs["config"])
        else:
            raise ValueError(f"Unknown transformation type: {transformation_type}")

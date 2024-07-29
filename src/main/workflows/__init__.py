from typing import List
from src.main.transformation import BaseTransformation


class Workflow:
    def __init__(self):
        self.transformations: List[BaseTransformation] = []

    def add_transformation(self, transformation: BaseTransformation):
        self.transformations.append(transformation)
        return self

    def execute(self):
        for transformation in self.transformations:
            transformation.apply()


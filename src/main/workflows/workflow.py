from typing import List

from src.main.transformation import TransformationFactory
from src.main.workflows import Workflow
from pyspark.sql import DataFrame
from src.main.configs import get_data_generator_config, get_anonymize_column_list


def create_workflow(spark_session, workflow_type, **kwargs):
    workflow = Workflow()

    if workflow_type == 'generate_and_anonymize':
        generator_config = get_data_generator_config(kwargs.get('arg_generator_config', None))
        anonymize_config = get_anonymize_column_list(kwargs.get('arg_anonymize_config', None))
        generator_transformation = (TransformationFactory
                                    .create_transformation(spark_session, "data_generation", config=generator_config))
        anonymize_transformation = (TransformationFactory
                                    .create_transformation(spark_session, "data_anonymize", config=anonymize_config))
        workflow.add_transformation(generator_transformation) \
            .add_transformation(anonymize_transformation)
        return workflow
    elif workflow_type == 'generate':
        generator_config = get_data_generator_config(kwargs.get('arg_generator_config', None))
        generator_transformation = (TransformationFactory
                                    .create_transformation(spark_session, "data_generation", config=generator_config))
        workflow.add_transformation(generator_transformation)
        return workflow
    elif workflow_type == 'anonymize':
        anonymize_config = get_anonymize_column_list(kwargs.get('arg_anonymize_config', None))
        anonymize_transformation = (TransformationFactory
                                    .create_transformation(spark_session, "data_anonymize", config=anonymize_config))
        workflow.add_transformation(anonymize_transformation)
        return workflow
    else:
        raise ValueError(f"Unknown workflow type: {workflow_type}")


def initiate_workflow(spark, workflow_type):
    create_workflow(spark, workflow_type).execute()




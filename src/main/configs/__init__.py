from src.main.configs.anonymize import DEFAULT_CONFIG as ANONYMIZE_CONFIG
from src.main.configs.data_generator import DEFAULT_CONFIG as DATA_GENERATOR_CONFIG
import json


def get_anonymize_column_list(column_list=None):
    return ANONYMIZE_CONFIG or column_list  # return whichever is true


def get_data_generator_config(config=None):
    return DATA_GENERATOR_CONFIG or config  # return whichever is true

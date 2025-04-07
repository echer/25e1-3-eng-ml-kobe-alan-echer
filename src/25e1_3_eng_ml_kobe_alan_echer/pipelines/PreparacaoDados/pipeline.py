"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes
from kedro.config import OmegaConfigLoader 

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.drop_columns_drop_na,
            inputs=['dataset_kobe_dev'],
            outputs='data_filtered_dev',
            tags=['preprocessing']
        ),
        node(
            nodes.drop_columns_drop_na,
            inputs=['dataset_kobe_prod'],
            outputs='data_filtered_prod',
            tags=['preprocessing']
        ),
        node(
            nodes.split_train_test,
            inputs=['data_filtered_dev'],
            outputs=['base_train_dev','base_test_dev'],
            tags=['preprocessing'],
        ),
        node(
            nodes.split_train_test,
            inputs=['data_filtered_prod'],
            outputs=['base_train_prod','base_test_prod'],
            tags=['preprocessing'],
        ),
    ])

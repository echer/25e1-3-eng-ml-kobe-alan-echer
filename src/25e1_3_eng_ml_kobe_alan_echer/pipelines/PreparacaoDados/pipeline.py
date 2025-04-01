"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes
from kedro.config import OmegaConfigLoader 

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def isProduction():
    return parameters['is_production']

def getRawDataset():
    return 'kobe_raw_dev@parquet' if(not isProduction()) else 'kobe_raw_prod@parquet'

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.drop_columns,
            inputs=[getRawDataset()],
            outputs='droped_columns',
        ),
        node(
            nodes.drop_columns,
            inputs=['droped_columns'],
            outputs='droped_na',
        ),
        node(
            nodes.split_train_test,
            inputs=['droped_na'],
            outputs=['base_train','base_test'],
        ),
        node(
            nodes.train_model,
            inputs=['base_train'],
            outputs=['trained_model_1', 'trained_model_2'],
        ),
    ])

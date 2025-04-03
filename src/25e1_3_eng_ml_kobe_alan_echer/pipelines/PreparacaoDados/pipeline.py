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
    return 'dataset_kobe_dev' if(not isProduction()) else 'dataset_kobe_prod'

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.drop_columns_drop_na,
            inputs=[getRawDataset()],
            outputs='data_filtered',
            tags=['preprocessing']
        ),
        node(
            nodes.split_train_test,
            inputs=['data_filtered'],
            outputs=['base_train','base_test'],
            tags=['preprocessing'],
        ),
    ])

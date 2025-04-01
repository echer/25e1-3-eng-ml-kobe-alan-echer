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
            nodes.kobe_intermediate_drop_columns,
            inputs=[getRawDataset()],
            outputs='kobe_intermediate_drop_columns',
            tags=['preprocessing'],
        ),
        node(
            nodes.kobe_intermediate_shot_made_flag_drop_na,
            inputs=['kobe_intermediate_drop_columns'],
            outputs='kobe_intermediate_shot_made_flag_drop_na',
            tags=['preprocessing'],
        ),
        node(
            nodes.kobe_raw_parquet_split_train_test,
            inputs=['kobe_intermediate_shot_made_flag_drop_na'],
            outputs=['base_train','base_test'],
            tags=['preprocessing'],
        ),
        node(
            nodes.train_model_pycarret,
            inputs=['base_train'],
            outputs='trained_model',
            tags='model'
        ),
    ])

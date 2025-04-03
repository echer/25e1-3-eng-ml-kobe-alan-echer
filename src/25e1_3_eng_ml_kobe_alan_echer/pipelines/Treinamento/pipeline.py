"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes
from kedro.config import OmegaConfigLoader 

parameters = OmegaConfigLoader(conf_source=".")['parameters']


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.train_models,
            inputs=['base_train'],
            outputs=['trained_best_model','trained_lr_model'],
            tags=['training'],
        ),
    ])

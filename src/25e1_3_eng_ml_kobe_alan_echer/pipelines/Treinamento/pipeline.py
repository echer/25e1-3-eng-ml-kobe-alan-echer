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
            nodes.train_model,
            inputs=['base_train'],
            outputs=['trained_model_1', 'trained_model_2'],
        ),
    ])

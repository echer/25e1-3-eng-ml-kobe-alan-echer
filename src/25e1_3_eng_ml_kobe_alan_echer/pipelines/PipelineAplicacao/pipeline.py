"""
This is a boilerplate pipeline 'PipelineAplicacao'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.train_models,
            inputs=['base_train_prod'],
            outputs=['trained_dt_model_prod','trained_lr_model_prod'],
            tags=['training_prod'],
        )
    ])

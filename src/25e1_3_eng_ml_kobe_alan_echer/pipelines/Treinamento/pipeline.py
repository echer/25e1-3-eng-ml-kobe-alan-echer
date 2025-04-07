"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.train_models,
            inputs=['base_train_dev'],
            outputs=['trained_dt_model_dev','trained_lr_model_dev'],
            tags=['training_dev'],
        ),
        node(
            nodes.get_metrics_dt_dev,
            inputs=['base_train_dev'],
            outputs='dt_metrics_dev',
            tags=['metrics']
        ),
        node(
            nodes.get_metrics_lr_dev,
            inputs=['base_train_dev'],
            outputs='lr_metrics_dev',
            tags=['metrics']
        ),
    ])

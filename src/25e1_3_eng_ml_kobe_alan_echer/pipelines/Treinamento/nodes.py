"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.12
"""

from pycaret.classification import *
from kedro.config import OmegaConfigLoader

parameters = OmegaConfigLoader(conf_source=".")['parameters']

# These models are trained together bacause kedro run nodes in paralel
# and while one experiment are runing we cannot run another one with same id
# causing the error on mlflow: 
# MlflowException: Cannot start run with ID x
# because active run ID does not match environment run
def train_models(dataset):
    return train_dt_model(dataset), train_lr_model(dataset)

def train_lr_model(dataset):
    experiment = ClassificationExperiment()
    experiment.setup(
        data=dataset,
        target=parameters['y_column'],
        log_experiment='mlflow', 
        experiment_name=parameters['mflow_experiment_name'], 
        session_id=parameters['session_id'],
        log_plots=True,
    )
    model = experiment.tune_model(
        experiment.create_model('lr'),
        optimize=parameters['tune_target_metric'],
        n_iter=parameters['tune_n_iter'],
        search_library='scikit-optimize',
    )
    experiment.plot_model(model, plot='auc', save='data/08_reporting/lr_model')
    return model

def train_dt_model(dataset):
    experiment = ClassificationExperiment()
    experiment.setup(
        data=dataset,
        target=parameters['y_column'],
        log_experiment='mlflow', 
        experiment_name=parameters['mflow_experiment_name'], 
        session_id=parameters['session_id'],
        log_plots=True,
    )
    model = experiment.tune_model(
        experiment.create_model('dt'),
        optimize=parameters['tune_target_metric'],
        n_iter=parameters['tune_n_iter'],
        search_library='scikit-optimize',
    )
    experiment.plot_model(model, plot='auc', save='data/08_reporting/dt_model')
    return model
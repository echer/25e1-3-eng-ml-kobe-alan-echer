"""
This is a boilerplate pipeline 'Treinamento'
generated using Kedro 0.19.12
"""

from pycaret.classification import *
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from kedro.config import OmegaConfigLoader

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def train_model(dataset):
    experiment = ClassificationExperiment()
    experiment.setup(
        data=dataset,
        target=parameters['y_column'],
        log_experiment='mlflow', 
        experiment_name=parameters['mflow_experiment_name'], 
        session_id=parameters['session_id'],
        log_plots=True,
        #log_profile=True,
        #log_data=True,
        #normalize=True,
        #normalize_method='robust',
        #polynomial_features=True,
        #feature_selection=True,
        #remove_multicollinearity=True,
        #pca=True,
    )
    best = experiment.compare_models(n_select=15)
    model_1 = None
    model_2 = None

    for model in best:
        if(isinstance(model, LogisticRegression)):
            model_1 = model
        if(isinstance(model, DecisionTreeClassifier)):
            model_2 = model

    return model_1, model_2
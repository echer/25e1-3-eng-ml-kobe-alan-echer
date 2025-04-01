"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.19.12
"""
from sklearn.model_selection import train_test_split
from kedro.config import OmegaConfigLoader 
from pycaret.classification import *
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def drop_columns(dataset):
    dataset = dataset.drop(columns=['action_type','combined_shot_type','game_event_id','game_id','loc_x','loc_y','season','seconds_remaining','shot_type','shot_zone_area','shot_zone_basic','shot_zone_range','team_id','team_name','game_date','matchup','opponent','shot_id'])
    return dataset

def drop_na(dataset):
    dataset = dataset.dropna()
    return dataset

def split_train_test(dataset):
    train, test = train_test_split(
        dataset, 
        test_size=parameters['train_test_split_ratio'], 
        stratify=dataset[parameters['y_column']]
    ) 
    return train, test

def train_model(dataset):
    experiment = ClassificationExperiment()
    experiment.setup(
        data=dataset,
        target=parameters['y_column'],
        log_experiment='mlflow', 
        experiment_name=parameters['mflow_experiment_name'], 
        session_id=parameters['session_id'])
    best = experiment.compare_models(n_select=15)
    model_1 = None
    model_2 = None

    for model in best:
        if(isinstance(model, LogisticRegression)):
            model_1 = model
        if(isinstance(model, DecisionTreeClassifier)):
            model_2 = model

    return model_1, model_2
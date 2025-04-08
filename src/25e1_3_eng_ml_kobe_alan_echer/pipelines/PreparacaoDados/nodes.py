"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.19.12
"""
from sklearn.model_selection import train_test_split
from kedro.config import OmegaConfigLoader 
import mlflow

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def drop_columns_drop_na(dataset):
    dataset = dataset.drop(columns=['action_type','combined_shot_type','game_event_id','game_id','loc_x','loc_y','season','seconds_remaining','shot_type','shot_zone_area','shot_zone_basic','shot_zone_range','team_id','team_name','game_date','matchup','opponent','shot_id'])
    dataset = dataset.dropna()
    return dataset

def split_train_test_dev(dataset):
    test_ratio = parameters['train_test_split_ratio'] * 100
    train_ratio = 100 - test_ratio
    train, test = train_test_split(
        dataset, 
        test_size=parameters['train_test_split_ratio'], 
        stratify=dataset[parameters['y_column']]
    ) 
    mlflow.log_metric("Base-de-Teste-PERCENT-DEV", test_ratio)
    mlflow.log_metric("Base-de-Treino-PERCENT-DEV", train_ratio)
    mlflow.log_metric("Base-de-Teste-QTD-DEV", test.shape[0])
    mlflow.log_metric("Base-de-Teste-QTD-DEV", train.shape[0])
    return train, test

def split_train_test_prod(dataset):
    test_ratio = parameters['train_test_split_ratio'] * 100
    train_ratio = 100 - test_ratio
    train, test = train_test_split(
        dataset, 
        test_size=parameters['train_test_split_ratio'], 
        stratify=dataset[parameters['y_column']]
    ) 
    mlflow.log_metric("Base-de-Teste-PERCENT-PROD", test_ratio)
    mlflow.log_metric("Base-de-Treino-PERCENT-PROD", train_ratio)
    mlflow.log_metric("Base-de-Teste-QTD-PROD", test.shape[0])
    mlflow.log_metric("Base-de-Teste-QTD-PROD", train.shape[0])
    return train, test
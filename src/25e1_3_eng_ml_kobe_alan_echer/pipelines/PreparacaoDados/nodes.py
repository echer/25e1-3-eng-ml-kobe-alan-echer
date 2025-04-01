"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.19.12
"""
from sklearn.model_selection import train_test_split
from kedro.config import OmegaConfigLoader 

parameters = OmegaConfigLoader(conf_source=".")['parameters']

def kobe_intermediate_drop_columns(dataset):
    dataset = dataset.drop(columns=['action_type','combined_shot_type','game_event_id','game_id','loc_x','loc_y','season','seconds_remaining','shot_type','shot_zone_area','shot_zone_basic','shot_zone_range','team_id','team_name','game_date','matchup','opponent','shot_id'])
    return dataset

def kobe_raw_parquet_split_train_test(dataset):
    train, test = train_test_split(
        dataset, 
        test_size=parameters['train_test_split_ratio'], 
        stratify=dataset[parameters['y_column']]
    ) 
    return train, test

def kobe_intermediate_shot_made_flag_drop_na(dataset):
    dataset = dataset.dropna()
    return dataset

def run_pycarret():
    pass
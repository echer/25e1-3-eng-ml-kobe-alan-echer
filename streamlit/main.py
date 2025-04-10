import streamlit as st
import requests
from kedro_datasets.pandas import ParquetDataset
import pandas as pd
import json

def call_inference(port, data):
    resp = requests.post(
        f'http://localhost:{port}/invocations',
        json=data
    )

    st.write(resp.status_code)
    #st.write(resp.json())

    inference = resp.json()
    return inference['predictions']

st.markdown("""
# Trabalho de Engenharia de Machine Learning - Alan Echer
            PREDIÇÕES DA BASE TESTE
""")

dataset = ParquetDataset(filepath='./data/05_model_input/base_test_prod.parquet').load()
dataset = dataset.drop(columns=['shot_made_flag'])

array = list(dataset.values)
inputs = json.loads(pd.Series(array).to_json(orient='split'))['data']
print(inputs)
payload = {
        'inputs':inputs,
    }

print(payload)

result = call_inference('5001', payload)

st.write(result)

#st.write('Acertou? ', {'Sim!' if(result) else 'Não!'})
import streamlit as st
import requests

def call_inference(port, data):
    send_data = {
        'inputs':[
            list(data.values())
        ],
    }
    
    resp = requests.post(
        f'http://localhost:{port}/invocations',
        json=send_data
    )

    st.write(resp.status_code)
    st.write(resp.json())

    inference = resp.json()
    return inference['predictions'][0]

st.markdown("""
# Trabalho de Engenharia de Machine Learning - Alan Echer
            
Esta página realiza inferencias sobre um modelo treinado com os dados dos arremessos do Kobe Bryant            
""")

lat = st.number_input('Latitude')
lon = st.number_input('Longitude')
minutes_remaining = st.number_input('Minutos restantes', min_value=0)
period = st.number_input('Periodo', min_value=0)
playoffs = st.radio('Jogo de eliminatória?',['Sim','Não'])
shot_distance = st.number_input('Distancia do arremesso', min_value=0)
modelo = st.radio('Modelo',['Arvore de Decisão','Regressão Logistica'])


data = {
    'lat':lat,
    'lon':lon,
    'minutes_remaining':minutes_remaining,
    'period':period,
    'playoffs':1 if(playoffs == 'Sim') else 0,
    'shot_distance':shot_distance,
}

st.json(list(data.values()))

if(modelo == 'Arvore de Decisão'):
    port = '5001'
elif(modelo == 'Regressão Logistica'):
    port = '5002'

result = call_inference(port, data)

st.write('Acertou? ', {'Sim!' if(result) else 'Não!'})
# 25e1-3-eng-ml-kobe-alan-echer

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)

## Overview

This is your new Kedro project, which was generated using `kedro 0.19.12`.

Take a look at the [Kedro documentation](https://docs.kedro.org) to get started.

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a data engineering convention
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.


## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/tutorial/package_a_project.html)

## Trabalho Engenharia de Machine Learning - Alan Echer ##

# (Link do repositorio)[https://github.com/echer/25e1-3-eng-ml-kobe-alan-echer.git] #

# Apontar os artefatos criados e sua composição detalhada #
# Se for dataset é importante falar as colunas descrição e os tipos de dados de cada coluna #
# Se for modelo descrever o modelo #
# Descrever a separacao de dados treino e teste #

# Artefato 1 (dataset_kobe{dev/prod}.parquet) - Dataset original dev e prod guardadas na pasta data/01_raw/, o dataset contém os registros dos arremessos do kobe bryant e um indicador para saber se acertou ou não. #

# Artefato 2 (data_filtered.parquet) - Dataset com dados filtrados, foram removidos dados nulos e algumas colunas dexando apenas as colunas abaixo: 
- lat - Latitude do jogador kobe
- lon - Longitude do jogador kobe
- minutes_remaining - Minutos restantes para o término da partida
- period - Periodo ou tempo da partida atual
- playoffs - Jogos de eliminatória
- shot_distance - Distancia do arremesso
- shot_made_flag - Indicador se fez acertou ou não o arremesso#

# Artefato 3 (base_train) - Dataset contendo 80% dos dados do dataset 'data_filtered' estratificando os dados baseado na coluna target shot_made_flag, o dataset segue a mesma estrutura do artefato 2.#

# Artefato 4 (base_test) - Dataset contendo 80% dos dados do dataset# 'data_filtered' estratificando os dados baseado na coluna target shot_made_flag, o dataset segue a mesma estrutura do artefato 2. #


diagrama: https://excalidraw.com/#room=cd3f01d539bfa6994444,bzKX0k0Hkq-9AGS60N83-Q

O aluno categorizou corretamente os dados?	

# OK - O aluno integrou a leitura dos dados corretamente à sua solução? #

O aluno aplicou o modelo em produção (servindo como API ou como solução embarcada)?	

O aluno indicou se o modelo é aderente a nova base de dados?

O aluno criou um repositório git com a estrutura de projeto baseado no Framework TDSP da Microsoft?	

O aluno criou um diagrama que mostra todas as etapas necessárias para a criação de modelos?	

# OK - O aluno treinou um modelo de regressão usando PyCaret e MLflow?	#

O aluno calculou o Log Loss para o modelo de regressão e registrou no mlflow?	

# OK - O aluno treinou um modelo de árvore de decisao usando PyCaret e MLflow?	#

O aluno calculou o Log Loss e F1 Score para o modelo de árvore de decisão e registrou no mlflow?	

O aluno indicou o objetivo e descreveu detalhadamente cada artefato criado no projeto?	

O aluno cobriu todos os artefatos do diagrama proposto?	

O aluno usou o MLFlow para registrar a rodada "Preparação de Dados" com as métricas e argumentos relevantes?	

O aluno removeu os dados faltantes da base?	

O aluno selecionou as colunas indicadas para criar o modelo?	

O aluno indicou quais as dimensões para a base preprocessada?	

O aluno criou arquivos para cada fase do processamento e os armazenou nas pastas indicadas?	

# OK - O aluno separou em duas bases, uma para treino e outra para teste #	

# OK - O aluno criou um pipeline chamado "Treinamento" no MlFlow?	#

O aluno identificou a diferença entre a base de desenvolvimento e produção?	

O aluno descreveu como monitorar a saúde do modelo no cenário com e sem a disponibilidade da variável alvo?	

O aluno implementou um dashboard de monitoramento da operação usando Streamlit?	

O aluno descreveu as estratégias reativa e preditiva de retreinamento para o modelo em operação?	

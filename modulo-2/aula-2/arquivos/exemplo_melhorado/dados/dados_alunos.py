# 📊 Data Lake - Dataset de Alunos
# Arquivo que contém os dados dos alunos para ser importado por outros módulos

import pandas as pd

# Dataset de alunos (como um data lake)
DADOS_ALUNOS = {
    "horas_estudo": [2, 4, 5, 1, 3, 6, 7, 8, 2, 5],
    "faltas":        [5, 3, 2, 8, 6, 1, 0, 1, 4, 2],
    "aprovado":      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
}

def carregar_dados():
    """
    Carrega os dados dos alunos do data lake
    Returns:
        pandas.DataFrame: DataFrame com os dados dos alunos
    """
    return pd.DataFrame(DADOS_ALUNOS)

def obter_features_target():
    """
    Separa features (X) e target (y) dos dados
    Returns:
        tuple: (X, y) onde X são as features e y é o target
    """
    df = carregar_dados()
    X = df[["horas_estudo", "faltas"]]
    y = df["aprovado"]
    return X, y 
# 🧠 Modelo de Aprovação - Machine Learning
# Arquivo com as funções de ML que importa dados do data lake

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from dados_alunos import obter_features_target

class ModeloAprovacao:
    def __init__(self):
        """Inicializa o modelo de aprovação"""
        self.modelo = LogisticRegression()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.acuracia = None
        
    def treinar_modelo(self, test_size=0.3, random_state=42):
        """
        Treina o modelo com os dados do data lake
        Args:
            test_size (float): Proporção de dados para teste
            random_state (int): Seed para reprodutibilidade
        """
        # Carregar dados do data lake
        X, y = obter_features_target()
        
        # Dividir em treino e teste
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Treinar modelo
        self.modelo.fit(self.X_train, self.y_train)
        
        # Calcular acurácia
        self.acuracia = self.modelo.score(self.X_test, self.y_test)
        
        return self.acuracia
    
    def prever_aprovacao(self, horas_estudo, faltas):
        """
        Prevê se um aluno será aprovado ou reprovado
        Args:
            horas_estudo (int): Número de horas de estudo
            faltas (int): Número de faltas
        Returns:
            str: "Aprovado" ou "Reprovado"
        """
        novo_aluno = [[horas_estudo, faltas]]
        resultado = self.modelo.predict(novo_aluno)
        return "Aprovado" if resultado[0] == 1 else "Reprovado"
    
    def prever_multiplos_alunos(self, horas_estudo_list, faltas_list):
        """
        Prevê aprovação para múltiplos alunos
        Args:
            horas_estudo_list (list): Lista de horas de estudo
            faltas_list (list): Lista de faltas
        """
        resultados = []
        for i in range(len(horas_estudo_list)):
            resultado = self.prever_aprovacao(horas_estudo_list[i], faltas_list[i])
            resultados.append(f"Aluno {i+1}: {resultado}")
        return resultados
    
    def obter_acuracia(self):
        """Retorna a acurácia do modelo"""
        return self.acuracia
    
    def mostrar_info_modelo(self):
        """Mostra informações sobre o modelo treinado"""
        print(f"📊 Informações do Modelo:")
        print(f"   - Acurácia: {self.acuracia:.2f}")
        print(f"   - Dados de treino: {len(self.X_train)} amostras")
        print(f"   - Dados de teste: {len(self.X_test)} amostras")
        print(f"   - Features: {list(self.X_train.columns)}")

# Função de conveniência para criar e treinar modelo rapidamente
def criar_modelo_treinado():
    """
    Cria e treina um modelo de aprovação
    Returns:
        ModeloAprovacao: Modelo treinado
    """
    modelo = ModeloAprovacao()
    modelo.treinar_modelo()
    return modelo 
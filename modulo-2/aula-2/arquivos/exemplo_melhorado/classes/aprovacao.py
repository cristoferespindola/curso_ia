import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#1. Criar dataset
dados = {
    "horas_estudo": [2, 4, 5, 1, 3, 6, 7, 8, 2, 5],
    "faltas":        [5, 3, 2, 8, 6, 1, 0, 1, 4, 2],
    "aprovado":      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(dados)

# 2. Separar features e target
X = df[["horas_estudo", "faltas"]]
y = df["aprovado"]

# 3. Dividir em treino e teste (70% treino / 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Criar modelo
modelo = LogisticRegression()

# 5. Treinar modelo
modelo.fit(X_train, y_train)

# 6. Testar modelo
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia: {acuracia:.2f}", flush=True)

# 7. Fazer previsão para um novo aluno
novo_aluno = [[4, 2]]  # 4 horas de estudo, 2 faltas
resultado = modelo.predict(novo_aluno)
print("Aprovado" if resultado[0] == 1 else "Reprovado", flush=True)


# funcao para prever se o aluno foi aprovado ou reprovado
def prever_aprovacao(horas_estudo, faltas):
    novo_aluno = [[horas_estudo, faltas]]
    resultado = modelo.predict(novo_aluno)
    return "Aprovado" if resultado[0] == 1 else "Reprovado"

# teste da funcao
print(prever_aprovacao(4, 2))

# funcao para prever varios alunos
def prever_aprovacao_multiplos(horas_estudo, faltas):
    for i in range(len(horas_estudo)):
        print(f"Aluno {i+1}: {prever_aprovacao(horas_estudo[i], faltas[i])}")

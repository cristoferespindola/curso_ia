# 🛠️ Aula 2.2 — Preparando o ambiente

## 📦 Instalação das bibliotecas

Instale as bibliotecas necessárias para Machine Learning:

```bash
pip install scikit-learn pandas
```

## 🧑‍💻 Código da sua primeira IA

Crie o arquivo: `modulo2-ml/aprovacao_alunos.py`

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# 1. Criar dataset
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
print(f"Acurácia: {acuracia:.2f}")

# 7. Fazer previsão para um novo aluno
novo_aluno = [[4, 2]]  # 4 horas de estudo, 2 faltas
resultado = modelo.predict(novo_aluno)
print("Aprovado" if resultado[0] == 1 else "Reprovado")
```

## 📋 TO-DOs

### ✅ **Tarefas obrigatórias:**

1. **📁 Criar estrutura:**
   - Criar a pasta `modulo2-ml/`
   - Salvar o script acima como `aprovacao_alunos.py`

2. **🚀 Executar código:**
   - Rodar o código e verificar a acurácia
   - Anotar o resultado obtido

3. **🔬 Experimentar:**
   - Alterar os dados de teste e ver como a acurácia muda
   - Testar diferentes configurações

### 🎯 **Tarefas extras:**

4. **🧪 Criar casos de teste:**
   - Criar pelo menos 3 novos casos de teste para `novo_aluno`
   - Exemplos:
     ```python
     # Caso 1: Aluno dedicado
     novo_aluno = [[8, 1]]  # 8 horas estudo, 1 falta
     
     # Caso 2: Aluno com dificuldades
     novo_aluno = [[2, 7]]  # 2 horas estudo, 7 faltas
     
     # Caso 3: Aluno mediano
     novo_aluno = [[5, 4]]  # 5 horas estudo, 4 faltas
     ```

## 🎯 Resultado esperado:

```
Acurácia: 0.67
Aprovado
```

## 💡 Dicas importantes:

- ✅ **Verifique a instalação** - Certifique-se que as bibliotecas estão instaladas
- ✅ **Use ambiente virtual** - Mantenha as dependências organizadas
- ✅ **Teste diferentes dados** - Experimente com novos alunos
- ✅ **Anote os resultados** - Compare as acurácias obtidas

---

**🚀 Próximo passo:** Vamos analisar os resultados e entender como o modelo funciona! 🧠


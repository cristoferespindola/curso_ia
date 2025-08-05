# 🧠 Scikit-learn - Machine Learning

## 📚 O que é o Scikit-learn?

**Scikit-learn** é a biblioteca Python mais popular para **Machine Learning**. Oferece ferramentas simples e eficientes para análise preditiva e aprendizado de máquina.

### 🎯 **Para que serve:**
- 🎓 **Classificação** - Prever categorias (aprovado/reprovado)
- 📊 **Regressão** - Prever valores numéricos (preço, temperatura)
- 🎯 **Clustering** - Agrupar dados similares
- 📈 **Redução de dimensionalidade** - Simplificar dados complexos
- 🔍 **Seleção de features** - Escolher as melhores variáveis

## 🚀 Instalação

```bash
pip install scikit-learn
```

## 🎯 Tipos de problemas

### 1. **Classificação** - "Que categoria é?"

```python
# Exemplo: Aprovação de alunos
# Entrada: horas_estudo, faltas
# Saída: Aprovado (1) ou Reprovado (0)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
```

### 2. **Regressão** - "Qual é o valor?"

```python
# Exemplo: Prever preço de casas
# Entrada: área, quartos, localização
# Saída: Preço (valor numérico)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
```

### 3. **Clustering** - "Quais são similares?"

```python
# Exemplo: Agrupar clientes por comportamento
# Entrada: idade, renda, gastos
# Saída: Grupo (1, 2, 3, ...)

from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
```

## 🔧 Fluxo básico de ML

### **1. Preparar dados**

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar dados
dados = {
    'horas_estudo': [2, 4, 5, 1, 3, 6, 7, 8, 2, 5],
    'faltas': [5, 3, 2, 8, 6, 1, 0, 1, 4, 2],
    'aprovado': [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(dados)

# Separar features e target
X = df[['horas_estudo', 'faltas']]  # Features
y = df['aprovado']                   # Target

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

### **2. Escolher modelo**

```python
# Para classificação
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Para regressão
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Para clustering
from sklearn.cluster import KMeans
```

### **3. Treinar modelo**

```python
# Criar modelo
modelo = LogisticRegression()

# Treinar
modelo.fit(X_train, y_train)
```

### **4. Fazer predições**

```python
# Predizer dados de teste
y_pred = modelo.predict(X_test)

# Predizer novos dados
novo_aluno = [[4, 2]]  # 4 horas, 2 faltas
resultado = modelo.predict(novo_aluno)
print("Aprovado" if resultado[0] == 1 else "Reprovado")
```

### **5. Avaliar performance**

```python
# Acurácia
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia: {acuracia:.2f}")

# Métricas detalhadas
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

## 🎯 Modelos principais

### **Classificação**

#### **1. Regressão Logística**
```python
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()
modelo.fit(X_train, y_train)
```

**Vantagens:**
- ✅ **Simples e rápido**
- ✅ **Interpretável** - coeficientes têm significado
- ✅ **Bom para dados lineares**

**Limitações:**
- ❌ **Só funciona bem** para relações lineares
- ❌ **Pode ter overfitting** com muitas features

#### **2. Árvore de Decisão**
```python
from sklearn.tree import DecisionTreeClassifier

modelo = DecisionTreeClassifier(max_depth=3)
modelo.fit(X_train, y_train)
```

**Vantagens:**
- ✅ **Fácil de entender** - regras claras
- ✅ **Funciona com dados não-lineares**
- ✅ **Não precisa normalizar dados**

**Limitações:**
- ❌ **Pode overfitting** facilmente
- ❌ **Instável** - pequenas mudanças afetam muito

#### **3. Random Forest**
```python
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)
```

**Vantagens:**
- ✅ **Muito robusto** - combina várias árvores
- ✅ **Bom para dados complexos**
- ✅ **Importância de features**

**Limitações:**
- ❌ **Menos interpretável**
- ❌ **Mais lento** para treinar

### **Regressão**

#### **1. Regressão Linear**
```python
from sklearn.linear_model import LinearRegression

modelo = LinearRegression()
modelo.fit(X_train, y_train)
```

#### **2. Random Forest Regressor**
```python
from sklearn.ensemble import RandomForestRegressor

modelo = RandomForestRegressor(n_estimators=100)
modelo.fit(X_train, y_train)
```

## 📊 Métricas de avaliação

### **Para Classificação:**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Acurácia - Porcentagem de acertos
acuracia = accuracy_score(y_test, y_pred)

# Precisão - Dos que previu positivo, quantos eram realmente?
precisao = precision_score(y_test, y_pred)

# Recall - Dos que eram realmente positivos, quantos acertou?
recall = recall_score(y_test, y_pred)

# F1-Score - Média harmônica entre precisão e recall
f1 = f1_score(y_test, y_pred)

print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
```

### **Para Regressão:**

```python
from sklearn.metrics import mean_squared_error, r2_score

# Erro quadrático médio
mse = mean_squared_error(y_test, y_pred)

# R² - Quão bem o modelo explica a variância
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")
```

## 🔧 Pré-processamento

### **1. Normalização/Standardização**

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# StandardScaler (z-score)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# MinMaxScaler (0-1)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### **2. Codificação de variáveis categóricas**

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# LabelEncoder (para target)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# OneHotEncoder (para features)
from sklearn.compose import ColumnTransformer

categorical_features = ['cidade']
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), categorical_features)],
    remainder='passthrough'
)
X_encoded = ct.fit_transform(X)
```

### **3. Tratamento de valores nulos**

```python
from sklearn.impute import SimpleImputer

# Preencher com média
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Preencher com mediana
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)
```

## 🎯 Validação cruzada

### **K-Fold Cross Validation**

```python
from sklearn.model_selection import cross_val_score

# 5-fold cross validation
scores = cross_val_score(modelo, X, y, cv=5)
print(f"Acurácia média: {scores.mean():.2f} (+/- {scores.std() * 2:.2f})")
```

### **Stratified K-Fold**

```python
from sklearn.model_selection import StratifiedKFold

# Mantém proporção das classes
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(modelo, X, y, cv=skf)
```

## 🔍 Seleção de features

### **1. Correlação**

```python
import pandas as pd

# Matriz de correlação
correlacao = df.corr()
print(correlacao['target'].sort_values(ascending=False))
```

### **2. Feature Importance (Random Forest)**

```python
from sklearn.ensemble import RandomForestClassifier

modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)

# Importância das features
importancia = modelo.feature_importances_
features = X.columns

for feature, imp in zip(features, importancia):
    print(f"{feature}: {imp:.3f}")
```

### **3. Seleção automática**

```python
from sklearn.feature_selection import SelectKBest, f_classif

# Selecionar as 5 melhores features
selector = SelectKBest(score_func=f_classif, k=5)
X_selected = selector.fit_transform(X, y)
```

## 💡 Dicas importantes

### **Boas práticas:**
- ✅ **Sempre divida** em treino/teste
- ✅ **Use validação cruzada** para avaliação robusta
- ✅ **Normalize dados** quando necessário
- ✅ **Teste múltiplos modelos** antes de escolher
- ✅ **Documente** os parâmetros usados

### **Comandos úteis:**
```python
# Informações do modelo
modelo.get_params()     # Parâmetros do modelo
modelo.coef_           # Coeficientes (regressão linear)
modelo.intercept_      # Intercepto
modelo.feature_importances_  # Importância (Random Forest)

# Salvando e carregando modelos
import joblib
joblib.dump(modelo, 'modelo.pkl')
modelo_carregado = joblib.load('modelo.pkl')
```

### **Pipeline completo:**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Pipeline: normalizar + treinar
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])

pipeline.fit(X_train, y_train)
acuracia = pipeline.score(X_test, y_test)
```

---

**🧠 Scikit-learn é a ferramenta essencial para Machine Learning em Python!** Oferece tudo que você precisa para criar modelos preditivos poderosos. 🚀

---

**📚 Referência:** [Documentação oficial do Scikit-learn](https://scikit-learn.org/stable/)

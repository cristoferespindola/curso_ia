# 🐼 Pandas - Manipulação de Dados

## 📚 O que é o Pandas?

**Pandas** é uma biblioteca Python fundamental para **análise e manipulação de dados**. É como uma "planilha inteligente" que permite trabalhar com dados de forma eficiente e poderosa.

### 🎯 **Para que serve:**
- 📊 **Análise de dados** - Explorar e entender datasets
- 🧹 **Limpeza de dados** - Corrigir problemas nos dados
- 🔄 **Transformação** - Modificar e reorganizar dados
- 📈 **Visualização** - Criar gráficos e tabelas
- 💾 **Importação/Exportação** - Ler e salvar dados em diferentes formatos

## 🚀 Instalação

```bash
pip install pandas
```

## 📋 Estruturas principais

### 1. **Series** - Lista com índice

```python
import pandas as pd

# Criando uma Series
idades = pd.Series([25, 30, 35, 40], index=['João', 'Maria', 'Pedro', 'Ana'])
print(idades)
# João     25
# Maria    30
# Pedro    35
# Ana      40
# dtype: int64
```

### 2. **DataFrame** - Tabela 2D (mais usado)

```python
# Criando um DataFrame
dados = {
    'nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'idade': [25, 30, 35, 40],
    'cidade': ['SP', 'RJ', 'MG', 'SP'],
    'salario': [3000, 4500, 3800, 5200]
}

df = pd.DataFrame(dados)
print(df)
```

## 🔧 Operações básicas

### **Criando DataFrames**

```python
# Método 1: Dicionário
dados = {
    'coluna1': [1, 2, 3],
    'coluna2': ['a', 'b', 'c']
}
df = pd.DataFrame(dados)

# Método 2: Lista de listas
dados = [[1, 'a'], [2, 'b'], [3, 'c']]
df = pd.DataFrame(dados, columns=['coluna1', 'coluna2'])

# Método 3: Lendo arquivo
df = pd.read_csv('dados.csv')
df = pd.read_excel('dados.xlsx')
```

### **Visualizando dados**

```python
# Primeiras linhas
print(df.head())      # Primeiras 5 linhas
print(df.head(3))     # Primeiras 3 linhas

# Últimas linhas
print(df.tail())      # Últimas 5 linhas

# Informações gerais
print(df.info())      # Tipos de dados e memória
print(df.describe())  # Estatísticas numéricas
print(df.shape)       # (linhas, colunas)
```

### **Selecionando dados**

```python
# Por coluna
print(df['nome'])           # Uma coluna
print(df[['nome', 'idade']]) # Múltiplas colunas

# Por linha
print(df.iloc[0])          # Primeira linha
print(df.iloc[0:3])        # Linhas 0, 1, 2

# Por condição
print(df[df['idade'] > 30])  # Pessoas com mais de 30 anos
print(df[df['cidade'] == 'SP'])  # Pessoas de SP
```

## 📊 Exemplos práticos

### **Dataset de alunos (como no nosso projeto)**

```python
import pandas as pd

# Criando dataset de alunos
dados_alunos = {
    'nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carla'],
    'horas_estudo': [5, 3, 7, 2, 6],
    'faltas': [2, 5, 1, 8, 3],
    'aprovado': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(dados_alunos)
print(df)
```

### **Análise exploratória**

```python
# Estatísticas básicas
print(df.describe())

# Contagem de aprovados/reprovados
print(df['aprovado'].value_counts())

# Média de horas de estudo por status
print(df.groupby('aprovado')['horas_estudo'].mean())

# Correlação entre variáveis
print(df.corr())
```

### **Filtros e condições**

```python
# Alunos aprovados
aprovados = df[df['aprovado'] == 1]
print(aprovados)

# Alunos com muitas horas de estudo
estudiosos = df[df['horas_estudo'] >= 5]
print(estudiosos)

# Alunos com poucas faltas E muitas horas
excelentes = df[(df['faltas'] <= 2) & (df['horas_estudo'] >= 5)]
print(excelentes)
```

## 🧹 Limpeza de dados

### **Verificando dados**

```python
# Valores nulos
print(df.isnull().sum())

# Valores únicos
print(df['cidade'].unique())

# Informações sobre tipos
print(df.dtypes)
```

### **Corrigindo problemas**

```python
# Preenchendo valores nulos
df['idade'].fillna(df['idade'].mean(), inplace=True)

# Removendo duplicatas
df.drop_duplicates(inplace=True)

# Convertendo tipos
df['idade'] = df['idade'].astype(int)
```

## 📈 Agregações e grupos

### **Agrupando dados**

```python
# Média de idade por cidade
media_por_cidade = df.groupby('cidade')['idade'].mean()
print(media_por_cidade)

# Múltiplas agregações
resumo = df.groupby('cidade').agg({
    'idade': ['mean', 'min', 'max'],
    'salario': ['mean', 'sum']
})
print(resumo)
```

### **Pivot tables**

```python
# Tabela cruzada
pivot = df.pivot_table(
    values='salario',
    index='cidade',
    columns='aprovado',
    aggfunc='mean'
)
print(pivot)
```

## 💾 Salvando e carregando dados

### **Formatos suportados**

```python
# CSV
df.to_csv('dados.csv', index=False)
df = pd.read_csv('dados.csv')

# Excel
df.to_excel('dados.xlsx', index=False)
df = pd.read_excel('dados.xlsx')

# JSON
df.to_json('dados.json')
df = pd.read_json('dados.json')

# Parquet (eficiente)
df.to_parquet('dados.parquet')
df = pd.read_parquet('dados.parquet')
```

## 🎯 Vantagens do Pandas

### ✅ **Eficiência:**
- **Rápido** - Otimizado em C
- **Memória eficiente** - Usa menos RAM
- **Operações vetorizadas** - Mais rápidas que loops

### ✅ **Flexibilidade:**
- **Múltiplos formatos** - CSV, Excel, JSON, etc.
- **Fácil manipulação** - Sintaxe intuitiva
- **Integração** - Funciona com outras bibliotecas

### ✅ **Análise poderosa:**
- **Estatísticas** - Funções prontas
- **Visualização** - Gráficos integrados
- **Machine Learning** - Compatível com scikit-learn

## 💡 Dicas importantes

### **Boas práticas:**
- ✅ **Sempre verifique** os dados com `.info()` e `.head()`
- ✅ **Use `.copy()`** quando modificar dados
- ✅ **Trate valores nulos** antes da análise
- ✅ **Documente** as transformações feitas

### **Comandos úteis:**
```python
# Informações rápidas
df.info()           # Tipos e memória
df.describe()       # Estatísticas
df.shape            # Dimensões
df.columns          # Nomes das colunas
df.index            # Índices

# Verificações
df.isnull().sum()   # Valores nulos
df.duplicated()     # Duplicatas
df.nunique()        # Valores únicos
```

### **Para Machine Learning:**
```python
# Separando features e target
X = df[['horas_estudo', 'faltas']]  # Features
y = df['aprovado']                   # Target

# Convertendo para numpy (se necessário)
X_array = X.values
y_array = y.values
```

---

**🐼 Pandas é essencial para qualquer projeto de dados em Python!** É a base para análise, limpeza e preparação de dados para Machine Learning. 🚀
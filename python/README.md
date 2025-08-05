# 🐍 Python - Guia Completo

Bem-vindo ao guia completo de Python! Aqui você encontrará dicas, conceitos e exemplos práticos organizados por tópicos.

## 📚 Índice

### 🚀 **Configuração Inicial**
- 🐍 [Instalação do Python](../modulo-1/submodulo-1A/aula%201A.1/instalacao_python.md)
- 🐍 [Criando um ambiente virtual](../modulo-1/submodulo-1A/aula%201A.3/criando_ambiente_virtual.md)
- 🧱 [Estrutura Básica de um Script Python](../modulo-1/submodulo-1A/aula%201A.4/estrura_basica.md)

### 🔤 **Manipulação de Dados**
- 🔤 [Manipulação de Strings](./manipulacao_strings.md)
  - F-strings e formatação moderna
  - Formatadores de string (`02d`, `.2f`, etc.)
  - Exemplos práticos de formatação
  - Tabela de formatadores

### 📊 **Bibliotecas Essenciais**
- 🐼 [Pandas](./pandas.md)
  - Manipulação e análise de dados
  - DataFrames e Series
  - Limpeza e transformação de dados
  - Integração com Machine Learning

- 🧠 [Scikit-learn](./sklearn.md)
  - Machine Learning supervisionado
  - Classificação e regressão
  - Modelos principais (LogisticRegression, RandomForest, etc.)
  - Avaliação e métricas

### 🔄 **Conceitos Avançados**
- 🔄 [Conceitos Fundamentais](./conceitos.md)
  - Recursão e funções
  - Dicas rápidas para terminal
  - Testes de código inline
  - Exemplos práticos

## 🚀 Como usar este guia

1. **Comece pela configuração** - Instale Python e configure seu ambiente
2. **Aprenda o básico** - Estrutura de scripts e manipulação de strings
3. **Explore as bibliotecas** - Pandas para dados, Scikit-learn para ML
4. **Pratique** - Use o terminal para testar rapidamente

## 💡 Dicas Rápidas

### Testando código no terminal:
```bash
python3 -c "print('Olá, Python!')"
```

### Formatando strings:
```python
nome = "Maria"
idade = 25
print(f"Olá {nome}, você tem {idade} anos")
```

### Formatando horários:
```python
hora = 9
minuto = 5
print(f"São {hora:02d}:{minuto:02d}")  # São 09:05
```

### Usando Pandas:
```python
import pandas as pd
df = pd.DataFrame({'coluna': [1, 2, 3]})
print(df.head())
```

### Usando Scikit-learn:
```python
from sklearn.linear_model import LogisticRegression
modelo = LogisticRegression()
print("Modelo criado!")
```

## 📖 Estrutura dos arquivos

```
python/
├── README.md                    # ← Este arquivo (menu principal)
├── manipulacao_strings.md       # F-strings e formatação
├── pandas.md                   # Manipulação de dados
├── sklearn.md                  # Machine Learning
└── conceitos.md               # Recursão e dicas

modulo-1/submodulo-1A/
├── aula 1A.1/
│   └── instalacao_python.md    # Instalação do Python
├── aula 1A.3/
│   └── criando_ambiente_virtual.md # Ambientes virtuais
└── aula 1A.4/
    └── estrura_basica.md       # Estrutura de scripts
```

## 🎯 Próximos passos

- [x] ✅ Configuração inicial (Python + venv)
- [x] ✅ Estrutura básica de scripts
- [x] ✅ Manipulação de strings
- [x] ✅ Pandas para dados
- [x] ✅ Scikit-learn para ML
- [x] ✅ Conceitos de recursão
- [ ] 📝 Adicionar mais tópicos de Python
- [ ] 📝 Criar exercícios práticos
- [ ] 📝 Adicionar exemplos avançados
- [ ] 📝 Incluir dicas de performance

## 🔗 Links Úteis

- [🐍 Python.org](https://www.python.org/) - Site oficial
- [📚 Python Documentation](https://docs.python.org/) - Documentação oficial
- [🐼 Pandas Documentation](https://pandas.pydata.org/) - Guia do Pandas
- [🧠 Scikit-learn Documentation](https://scikit-learn.org/) - Guia do Scikit-learn
- [🎓 Real Python](https://realpython.com/) - Tutoriais excelentes

---

**Dica:** Use `Ctrl+F` (ou `Cmd+F`) para buscar rapidamente nos arquivos! 🔍
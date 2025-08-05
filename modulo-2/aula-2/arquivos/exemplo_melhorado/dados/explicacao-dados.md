# 📊 Estrutura dos Dados - Dataset de Alunos

## 🎯 Como os Dados Estão Organizados

Cada posição do array representa um aluno diferente. Os dados estão estruturados como uma **matriz** onde:

```python
dados = {
    "horas_estudo": [2, 4, 5, 1, 3, 6, 7, 8, 2, 5],  # Posição 0 = aluno 1, posição 1 = aluno 2, etc.
    "faltas":        [5, 3, 2, 8, 6, 1, 0, 1, 4, 2],  # Posição 0 = aluno 1, posição 1 = aluno 2, etc.
    "aprovado":      [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]   # Posição 0 = aluno 1, posição 1 = aluno 2, etc.
}
```

## 📋 Tabela de Alunos

| Aluno | Horas de Estudo | Faltas | Aprovado | Status |
|-------|----------------|--------|----------|--------|
| 1     | 2              | 5      | 0        | ❌ Reprovado |
| 2     | 4              | 3      | 0        | ❌ Reprovado |
| 3     | 5              | 2      | 1        | ✅ Aprovado |
| 4     | 1              | 8      | 0        | ❌ Reprovado |
| 5     | 3              | 6      | 0        | ❌ Reprovado |
| 6     | 6              | 1      | 1        | ✅ Aprovado |
| 7     | 7              | 0      | 1        | ✅ Aprovado |
| 8     | 8              | 1      | 1        | ✅ Aprovado |
| 9     | 2              | 4      | 0        | ❌ Reprovado |
| 10    | 5              | 2      | 1        | ✅ Aprovado |

## 🔍 Padrões Identificados

O modelo de Machine Learning aprendeu os seguintes padrões:

### ✅ Alunos Aprovados:
- **Aluno 3**: 5 horas de estudo, 2 faltas
- **Aluno 6**: 6 horas de estudo, 1 falta  
- **Aluno 7**: 7 horas de estudo, 0 faltas
- **Aluno 8**: 8 horas de estudo, 1 falta
- **Aluno 10**: 5 horas de estudo, 2 faltas

### ❌ Alunos Reprovados:
- **Aluno 1**: 2 horas de estudo, 5 faltas
- **Aluno 2**: 4 horas de estudo, 3 faltas
- **Aluno 4**: 1 hora de estudo, 8 faltas
- **Aluno 5**: 3 horas de estudo, 6 faltas
- **Aluno 9**: 2 horas de estudo, 4 faltas

## 🧠 Lógica do Modelo

O algoritmo aprendeu que:
- **Mais horas de estudo** + **Menos faltas** = **Maior chance de aprovação**
- **Menos horas de estudo** + **Mais faltas** = **Maior chance de reprovação**

## 🎯 Exemplo de Previsão

Quando testamos com um novo aluno:
```python
novo_aluno = [[4, 2]]  # 4 horas de estudo, 2 faltas
```

O modelo prevê: **✅ Aprovado**

Porque o padrão (4 horas, 2 faltas) é similar aos alunos aprovados como o Aluno 3 e Aluno 10! 
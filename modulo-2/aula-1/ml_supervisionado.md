# 📘 Aula 2.1 — O que é Machine Learning supervisionado?

## 🎯 No aprendizado supervisionado:

- **Você fornece dados de entrada (features)**
- **Fornece a resposta correta (target)**
- **O algoritmo aprende a mapear entrada → saída**
- **Depois, ele prevê saídas para novos dados**

## 📊 Exemplo prático — Prever se um aluno vai passar ou não

### 💡 Ideia:
Baseado nas **horas de estudo** e nas **faltas**, prever se o aluno será **Aprovado (1)** ou **Reprovado (0)**.

### 🔍 Como funciona:

```python
# Dados de exemplo
alunos = [
    {"horas_estudo": 5, "faltas": 2, "aprovado": 1},  # Aprovado
    {"horas_estudo": 2, "faltas": 8, "aprovado": 0},  # Reprovado
    {"horas_estudo": 7, "faltas": 1, "aprovado": 1},  # Aprovado
    {"horas_estudo": 1, "faltas": 10, "aprovado": 0}  # Reprovado
]
```

### 🧠 Processo de aprendizado:

1. **📥 Entrada (Features):**
   - Horas de estudo
   - Número de faltas

2. **🎯 Saída (Target):**
   - Aprovado (1) ou Reprovado (0)

3. **🔄 Treinamento:**
   - Algoritmo analisa os padrões
   - Aprende: "mais estudo + menos faltas = aprovação"

4. **🔮 Previsão:**
   - Novo aluno: 6 horas estudo, 3 faltas
   - Modelo prevê: **Aprovado**

## ✅ Vantagens do ML Supervisionado:

- ✅ **Alto controle** - Você define o que quer prever
- ✅ **Resultados claros** - Saída específica (0 ou 1)
- ✅ **Fácil avaliação** - Pode medir acurácia
- ✅ **Interpretável** - Entende como o modelo decide

## 🎯 Aplicações comuns:

- 📊 **Classificação:** Email spam/não spam
- 🏥 **Diagnóstico:** Doença presente/ausente
- 💳 **Fraude:** Transação fraudulenta/normal
- 🎓 **Educação:** Aprovação/reprovação
- 🏠 **Imóveis:** Preço alto/baixo

---

**💡 Dica:** O ML supervisionado é como ensinar uma criança com exemplos - você mostra muitos casos e ela aprende o padrão! 🧠✨


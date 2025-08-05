# 🚀 Como usar o projeto de Machine Learning

Este guia mostra como configurar e executar o projeto de aprovação de alunos usando **ambiente virtual** e **pip**, evitando os erros que encontramos anteriormente.

## 📁 Estrutura do projeto

```
exemplo_melhorado/
├── como_usar.md           # ← Este arquivo
├── main.py                # Arquivo principal
├── classes/
│   ├── aprovacao.py       # Funções de aprovação
│   └── modelo_aprovacao.py # Classe do modelo ML
└── dados/
    ├── dados_alunos.py    # Data lake
    └── explicacao-dados.md # Explicação dos dados
```

## 🛠️ Configuração do ambiente

### 1. **Criar ambiente virtual**

```bash
# Navegar para a pasta do projeto
cd modulo-2/aula-2/arquivos/exemplo_melhorado

# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### 2. **Instalar dependências**

```bash
# Com ambiente virtual ativado
pip install pandas scikit-learn

# Verificar instalação
pip list
```

### 3. **Verificar se tudo está funcionando**

```bash
# Testar importações
python3 -c "import pandas as pd; print('pandas OK')"
python3 -c "from sklearn.model_selection import train_test_split; print('sklearn OK')"
```

## 🚀 Executando o projeto

### **Opção 1: Executar arquivo principal**

```bash
# Com ambiente virtual ativado
python3 main.py
```

### **Opção 2: Executar módulos separadamente**

```bash
# Testar apenas o modelo
python3 -c "
from classes.modelo_aprovacao import criar_modelo_treinado
modelo = criar_modelo_treinado()
print('Modelo criado com sucesso!')
"
```

### **Opção 3: Testar dados**

```bash
# Verificar dados
python3 -c "
from dados.dados_alunos import carregar_dados
df = carregar_dados()
print(f'Dataset carregado: {len(df)} alunos')
"
```

## 🔧 Solução de problemas

### ❌ **Erro: "externally-managed-environment"**

**Problema:** Tentando instalar sem ambiente virtual
```bash
pip install pandas scikit-learn
# Error: externally-managed-environment
```

**Solução:** Use ambiente virtual
```bash
# 1. Criar ambiente virtual
python3 -m venv venv

# 2. Ativar ambiente virtual
source venv/bin/activate

# 3. Agora instalar
pip install pandas scikit-learn
```

### ❌ **Erro: "source: no such file or directory"**

**Problema:** Caminho incorreto para ativar ambiente virtual
```bash
source aula-2/bin/activate  # ❌ Erro
```

**Solução:** Verificar onde está o ambiente virtual
```bash
# 1. Verificar se existe
ls -la

# 2. Ativar corretamente
source venv/bin/activate  # ✅ Correto
```

### ❌ **Erro: "ModuleNotFoundError"**

**Problema:** Bibliotecas não instaladas no ambiente virtual
```bash
python3 -c "import pandas"
# ModuleNotFoundError: No module named 'pandas'
```

**Solução:** Instalar no ambiente virtual ativado
```bash
# 1. Ativar ambiente virtual
source venv/bin/activate

# 2. Verificar se está ativo (deve mostrar (venv) no prompt)
# (venv) user@computer:~/projeto$

# 3. Instalar bibliotecas
pip install pandas scikit-learn

# 4. Testar
python3 -c "import pandas; print('OK')"
```

## 📊 Resultado esperado

Quando tudo estiver funcionando, você verá:

```
🎓 Sistema de Previsão de Aprovação
==================================================

📊 1. Carregando dados do data lake...
   - Dataset carregado com 10 alunos
   - Colunas: ['horas_estudo', 'faltas', 'aprovado']

🔧 2. Preparando dados para ML...
   - Features: ['horas_estudo', 'faltas']
   - Target: aprovado

🧠 3. Treinando modelo de ML...
📊 Informações do Modelo:
   - Acurácia: 0.67
   - Dados de treino: 7 amostras
   - Dados de teste: 3 amostras
   - Features: ['horas_estudo', 'faltas']

🎯 4. Testando previsões individuais...
   - Aluno com 4h estudo, 2 faltas: Aprovado
   - Aluno com 1h estudo, 8 faltas: Reprovado
   - Aluno com 7h estudo, 0 faltas: Aprovado
   - Aluno com 3h estudo, 5 faltas: Reprovado

👥 5. Testando previsões múltiplas...
   - Aluno 1: Reprovado
   - Aluno 2: Aprovado
   - Aluno 3: Aprovado
   - Aluno 4: Reprovado
   - Aluno 5: Aprovado

✅ Testes concluídos com sucesso!
```

## 💡 Dicas importantes

### ✅ **Boas práticas:**
- Sempre use ambiente virtual para projetos Python
- Ative o ambiente virtual antes de instalar bibliotecas
- Verifique se o ambiente está ativo (deve mostrar `(venv)` no prompt)
- Use `pip list` para verificar bibliotecas instaladas

### ⚠️ **Cuidados:**
- Não instale bibliotecas globalmente sem necessidade
- Sempre ative o ambiente virtual antes de executar o projeto
- Verifique o caminho correto para ativar o ambiente virtual

### 🔍 **Comandos úteis:**
```bash
# Verificar se ambiente virtual está ativo
echo $VIRTUAL_ENV

# Ver bibliotecas instaladas
pip list

# Desativar ambiente virtual
deactivate

# Verificar versão do Python
python3 --version
```

---

**🎉 Parabéns!** Agora você tem um ambiente Python organizado e funcional para Machine Learning! 🚀

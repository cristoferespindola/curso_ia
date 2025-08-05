# 🐍 Aula 1A.2 — Executando Código Python

> **Vamos aprender as diferentes formas de executar código Python e dar vida aos seus primeiros programas!**

---

## 🎯 Objetivos da Aula

Nesta aula você vai aprender:
- ✅ **Executar Python** no terminal interativo
- ✅ **Criar arquivos** `.py` e executá-los
- ✅ **Diferenças** entre modo interativo e script
- ✅ **Boas práticas** para desenvolvimento

---

## 💻 Opção 1: Terminal Interativo (Python Shell)

### **O que é?**
O terminal interativo permite executar código Python **linha por linha**, ideal para testes rápidos e experimentação.

### **Como usar:**

1. **Abra o terminal** e digite:
```bash
python
```

2. **Você verá algo assim:**
```
Python 3.10.x (default, ...)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

3. **Digite seu código:**
```python
>>> print("Olá IA!")
>>> 2 + 2
>>> nome = "Cristofer"
>>> print(f"Olá, {nome}!")
```

### **💡 Vantagens:**
- ⚡ **Rápido** para testes
- 🔍 **Feedback imediato**
- 🧪 **Ideal para experimentação**
- 📚 **Ótimo para aprender**

### **⚠️ Limitações:**
- ❌ **Código não é salvo**
- ❌ **Não ideal para projetos grandes**
- ❌ **Difícil de compartilhar**

---

## 📁 Opção 2: Arquivos .py (Scripts)

### **O que é?**
Arquivos `.py` são **scripts Python** que podem ser executados múltiplas vezes e compartilhados com outros.

### **Passo a Passo:**

#### **1. Criar o arquivo**
Crie um arquivo chamado `teste.py` com o seguinte conteúdo:

```python
# Meu primeiro programa Python
print("Olá, mundo da IA!")

# Variáveis
nome = "Cristofer"
idade = 25

# String formatada
print(f"Olá, {nome}! Você tem {idade} anos.")

# Operações matemáticas
resultado = 10 + 5
print(f"10 + 5 = {resultado}")
```

#### **2. Executar no terminal**
```bash
python teste.py
```

#### **3. Resultado esperado:**
```
Olá, mundo da IA!
Olá, Cristofer! Você tem 25 anos.
10 + 5 = 15
```

### **💡 Vantagens:**
- ✅ **Código salvo** permanentemente
- ✅ **Reutilizável** múltiplas vezes
- ✅ **Compartilhável** com outros
- ✅ **Ideal para projetos**
- ✅ **Versionamento** com Git

---

## 🔄 Comparação: Interativo vs Script

| Aspecto | Terminal Interativo | Arquivo .py |
|---------|-------------------|-------------|
| **Velocidade** | ⚡ Muito rápido | 🐌 Um pouco mais lento |
| **Persistência** | ❌ Não salva | ✅ Salva permanentemente |
| **Reutilização** | ❌ Não reutilizável | ✅ Reutilizável |
| **Compartilhamento** | ❌ Difícil | ✅ Fácil |
| **Projetos grandes** | ❌ Não recomendado | ✅ Ideal |
| **Aprendizado** | ✅ Ótimo para testes | ✅ Ótimo para prática |

---

## 🎯 Quando Usar Cada Opção?

### **Use Terminal Interativo quando:**
- 🧪 **Testando** uma função ou comando
- 🔍 **Explorando** uma biblioteca
- 📚 **Aprendendo** novos conceitos
- ⚡ **Precisando** de feedback rápido

### **Use Arquivos .py quando:**
- 📁 **Criando** um projeto
- 💾 **Precisando** salvar o código
- 🤝 **Compartilhando** com outros
- 🔄 **Executando** o mesmo código várias vezes

---

## 🚀 Prática Recomendada

### **Para Iniciantes:**
1. **Comece** com o terminal interativo para aprender
2. **Experimente** comandos e conceitos
3. **Quando confortável**, crie arquivos `.py`
4. **Combine** ambos conforme necessário

### **Exemplo de Fluxo:**
```bash
# 1. Teste no terminal
python
>>> def saudacao(nome):
...     return f"Olá, {nome}!"
>>> saudacao("Cristofer")
'Olá, Cristofer!'

# 2. Crie arquivo quando funcionar
# arquivo: saudacoes.py
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Cristofer"))
```

---

## 💡 Dicas Importantes

### ✅ **Boas Práticas:**
- **Sempre teste** no interativo primeiro
- **Use nomes descritivos** para arquivos
- **Comente seu código** para explicar
- **Mantenha** seus arquivos organizados

### ⚠️ **Cuidados:**
- **Não esqueça** de salvar arquivos
- **Verifique** se está no diretório correto
- **Use** extensão `.py` para arquivos Python
- **Teste** sempre antes de compartilhar

---

## 🎯 Desafio da Aula

**Crie seu primeiro programa Python!**

1. **Abra o terminal** e teste:
```python
python
>>> print("Meu primeiro código Python!")
>>> nome = input("Digite seu nome: ")
>>> print(f"Olá, {nome}! Bem-vindo ao mundo da IA!")
```

2. **Crie um arquivo** `meu_primeiro_programa.py`:
```python
# Meu primeiro programa Python
print("=== Bem-vindo ao Mundo da IA ===")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"\nOlá, {nome}!")
print(f"Você tem {idade} anos.")
print("Você está no caminho para se tornar um especialista em IA!")

# Calculadora simples
num1 = float(input("\nDigite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2

print(f"A soma de {num1} + {num2} = {soma}")
```

3. **Execute o arquivo:**
```bash
python meu_primeiro_programa.py
```

---

> **🎉 Parabéns! Você já sabe executar código Python de duas formas diferentes!**

---

*Próxima aula: Vamos aprender sobre variáveis, tipos de dados e estruturas de controle!*
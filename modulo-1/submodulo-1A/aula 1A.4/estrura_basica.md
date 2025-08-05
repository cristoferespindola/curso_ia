# 🧱 Aula 1A.4 — Estrutura Básica de um Script Python

> **Vamos aprender os blocos fundamentais que compõem qualquer programa Python e como organizá-los de forma profissional!**

---

## 🎯 Objetivos da Aula

Nesta aula você vai dominar:
- ✅ **Variáveis** e tipos de dados
- ✅ **Funções** e sua estrutura
- ✅ **Estruturas de controle** (if, for, while)
- ✅ **Organização** de código Python
- ✅ **Boas práticas** de programação

---

## 📚 Componentes Básicos de um Script Python

### **1. Variáveis - Onde Guardamos Informações**

Variáveis são como **caixas** onde armazenamos dados que queremos usar depois.

```python
# Variáveis básicas
nome = "John Doe"
idade = 30
altura = 1.75
eh_programador = True

# Variáveis com nomes descritivos
primeiro_nome = "John""
sobrenome = "Doe"
idade_atual = 30
profissao = "Desenvolvedor"
```

### **2. Funções - Blocos de Código Reutilizáveis**

Funções são como **receitas** que fazem uma tarefa específica.

```python
# Função simples
def saudacao(pessoa):
    return f"Olá, {pessoa}!"

# Função com múltiplos parâmetros
def apresentacao(nome, idade, profissao):
    return f"Meu nome é {nome}, tenho {idade} anos e sou {profissao}."

# Função com lógica condicional
def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"
```

### **3. Estruturas de Controle - Tomando Decisões**

Estruturas de controle permitem que o programa **tome decisões** baseadas em condições.

```python
# Condicional simples
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Condicional com múltiplas opções
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

# Loop for - repetindo ações
for i in range(5):
    print(f"Contagem: {i}")

# Loop while - repetindo até uma condição
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1
```

---

## 🎯 Exemplo Completo: Script de Apresentação

Vamos criar um script completo que demonstra todos os conceitos:

```python
# ==========================================
# SCRIPT DE APRESENTAÇÃO - EXEMPLO COMPLETO
# ==========================================

# 1. VARIÁVEIS - Dados da pessoa
nome = "Cristofer"
idade = 30
profissao = "Desenvolvedor"
hobbies = ["programação", "música", "esportes"]

# 2. FUNÇÕES - Lógica do programa
def saudacao(nome_pessoa):
    """Retorna uma saudação personalizada"""
    return f"Olá, {nome_pessoa}! Bem-vindo ao mundo da IA!"

def verificar_idade(idade_pessoa):
    """Verifica se a pessoa é maior de idade"""
    if idade_pessoa >= 18:
        return "Você é maior de idade"
    else:
        return "Você é menor de idade"

def apresentacao_completa(nome_pessoa, idade_pessoa, profissao_pessoa, hobbies_pessoa):
    """Cria uma apresentação completa"""
    resultado = f"""
=== APRESENTAÇÃO ===
Nome: {nome_pessoa}
Idade: {idade_pessoa} anos
Profissão: {profissao_pessoa}
Status: {verificar_idade(idade_pessoa)}
Hobbies: {', '.join(hobbies_pessoa)}
==================
"""
    return resultado

# 3. ESTRUTURAS DE CONTROLE - Lógica do programa
def main():
    """Função principal do programa"""
    
    # Saudação inicial
    print(saudacao(nome))
    print()
    
    # Verificação de idade
    status_idade = verificar_idade(idade)
    print(f"Status: {status_idade}")
    print()
    
    # Apresentação completa
    apresentacao = apresentacao_completa(nome, idade, profissao, hobbies)
    print(apresentacao)
    
    # Loop para mostrar hobbies
    print("Seus hobbies são:")
    for i, hobby in enumerate(hobbies, 1):
        print(f"{i}. {hobby}")
    
    # Condicional baseada na profissão
    if profissao.lower() == "desenvolvedor":
        print("\n🎉 Parabéns! Você já é um desenvolvedor!")
        print("Agora vamos aprender IA para expandir suas habilidades!")
    else:
        print(f"\n💡 Interessante! Você trabalha como {profissao}")
        print("A IA pode complementar muito bem sua área!")

# 4. EXECUÇÃO DO PROGRAMA
if __name__ == "__main__":
    main()
```

---

## 💡 Boas Práticas de Organização

### **✅ Estrutura Recomendada:**

```python
# 1. IMPORTS (se houver)
import datetime

# 2. VARIÁVEIS GLOBAIS
NOME_EMPRESA = "TechCorp"
VERSIONE = "1.0"

# 3. FUNÇÕES AUXILIARES
def funcao_auxiliar():
    pass

# 4. FUNÇÃO PRINCIPAL
def main():
    pass

# 5. EXECUÇÃO
if __name__ == "__main__":
    main()
```

### **✅ Convenções de Nomenclatura:**

| Tipo | Exemplo | Padrão |
|------|---------|--------|
| **Variáveis** | `nome_usuario` | snake_case |
| **Funções** | `calcular_soma()` | snake_case |
| **Constantes** | `PI = 3.14` | UPPER_CASE |
| **Classes** | `class Usuario:` | PascalCase |

---

## 🎯 Conceitos Importantes

### **📊 Tipos de Dados Básicos:**

```python
# String - texto
nome = "Cristofer"

# Integer - número inteiro
idade = 30

# Float - número decimal
altura = 1.75

# Boolean - verdadeiro/falso
eh_programador = True

# List - lista de itens
hobbies = ["programação", "música"]

# Dictionary - pares chave-valor
usuario = {"nome": "Cristofer", "idade": 30}
```

### **🔧 Estruturas de Controle Avançadas:**

```python
# Try/Except - tratamento de erros
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero!")

# For com enumerate
for indice, item in enumerate(["a", "b", "c"]):
    print(f"Item {indice}: {item}")

# List comprehension
quadrados = [x**2 for x in range(5)]
```

---

## 🚀 Prática Recomendada

### **Para Iniciantes:**
1. **Comece simples** - uma variável, uma função
2. **Teste cada parte** antes de continuar
3. **Use nomes descritivos** para variáveis e funções
4. **Comente seu código** para explicar a lógica
5. **Organize** em seções lógicas

### **Exemplo de Evolução:**
```python
# Versão 1: Simples
nome = "Cristofer"
print(f"Olá, {nome}!")

# Versão 2: Com função
def saudar(nome):
    return f"Olá, {nome}!"

print(saudar("Cristofer"))

# Versão 3: Com validação
def saudar(nome):
    if nome:
        return f"Olá, {nome}!"
    else:
        return "Olá, visitante!"

print(saudar("Cristofer"))
```

---

## 💡 Dicas Importantes

### ✅ **Boas Práticas:**
- **Sempre use nomes descritivos** para variáveis e funções
- **Mantenha funções pequenas** e com uma responsabilidade
- **Comente seu código** para explicar a lógica
- **Teste cada parte** antes de continuar
- **Organize** seu código em seções lógicas

### ⚠️ **Cuidados:**
- **Não use nomes genéricos** como `a`, `b`, `x`
- **Evite funções muito longas** - quebre em partes menores
- **Não esqueça** de indentar corretamente
- **Teste** sempre seu código

---

## 🎯 Desafio da Aula

**Crie um script de perfil pessoal!**

Use todos os conceitos aprendidos para criar um script que:
- Armazene suas informações pessoais
- Tenha funções para apresentação
- Use estruturas de controle para validações
- Tenha uma interface amigável

---

> **🎉 Parabéns! Você agora entende a estrutura fundamental de qualquer programa Python!**

---

*Próxima aula: Vamos praticar com exercícios e projetos para consolidar seu conhecimento!*
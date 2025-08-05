# 📝 Exercícios - Aula 1A.4: Estrutura Básica da Linguagem

> **Vamos consolidar tudo que você aprendeu com exercícios práticos e um projeto final!**

---

## 🎯 Objetivo dos Exercícios

Estes exercícios vão **testar e consolidar** seu conhecimento sobre Python básico. Cada exercício foi criado para reforçar conceitos específicos e preparar você para projetos mais avançados.

### ✨ **O que você vai praticar:**
- 📚 **Criar documentação** do seu aprendizado
- 💻 **Desenvolver projetos** práticos
- 🧠 **Aplicar conceitos** em situações reais
- 📊 **Organizar conhecimento** de forma estruturada

---

## 📋 Exercício 1: Documentação do Aprendizado

### **Objetivo:**
Criar um arquivo de anotações que servirá como **referência pessoal** para seus estudos futuros.

### **Tarefa:**
Crie o arquivo `anotacoes/python_basico.md` com os seguintes tópicos:

```markdown
# 📚 Python Básico - Minhas Anotações

## 🐍 Como Instalar o Python
- Site oficial: python.org
- Versão recomendada: 3.10+
- Marcar "Add Python to PATH"
- Verificar instalação: `python --version`

## 🔧 Como Criar e Ativar Ambiente Virtual
- Comando: `python -m venv nome_ambiente`
- Ativação Windows: `ambiente\Scripts\activate`
- Ativação macOS/Linux: `source ambiente/bin/activate`
- Desativação: `deactivate`

## 💻 Como Rodar Scripts Python
- Terminal interativo: `python`
- Arquivo .py: `python arquivo.py`
- Diferenças entre os dois métodos
- Vantagens de cada abordagem

## 📖 Sintaxe Básica
### Variáveis
- Tipos: int, float, str, bool
- Nomenclatura: snake_case
- Exemplos práticos

### Funções
- Definição: `def nome_funcao():`
- Parâmetros e retorno
- Escopo de variáveis

### Estruturas de Controle
- if/elif/else
- for loops
- while loops
- Exemplos práticos

### Print e Input
- Formatação de strings
- f-strings
- Entrada do usuário
```

### **💡 Dicas:**
- ✅ **Seja detalhado** - inclua exemplos de código
- ✅ **Use suas próprias palavras** - não copie, entenda
- ✅ **Adicione exemplos práticos** - casos de uso reais
- ✅ **Mantenha organizado** - use títulos e subtítulos

---

## 🎯 Exercício 2: Projeto Prático - Calculadora Avançada

### **Objetivo:**
Criar uma calculadora que demonstre domínio de **variáveis, funções e estruturas de controle**.

### **Especificações:**
Crie um arquivo `calculadora_avancada.py` com as seguintes funcionalidades:

```python
# Calculadora Avançada - Projeto Python Básico

def menu():
    """Exibe o menu principal da calculadora"""
    print("=== CALCULADORA AVANÇADA ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Raiz quadrada")
    print("7. Sair")
    return input("Escolha uma opção: ")

def obter_numeros():
    """Solicita e valida entrada de números"""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        print("❌ Erro: Digite apenas números válidos!")
        return None, None

def soma(a, b):
    """Realiza soma de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Realiza multiplicação de dois números"""
    return a * b

def divisao(a, b):
    """Realiza divisão de dois números"""
    if b == 0:
        return "❌ Erro: Divisão por zero!"
    return a / b

def potenciacao(a, b):
    """Realiza potenciação"""
    return a ** b

def raiz_quadrada(a):
    """Calcula raiz quadrada"""
    if a < 0:
        return "❌ Erro: Não existe raiz quadrada de número negativo!"
    return a ** 0.5

def main():
    """Função principal da calculadora"""
    while True:
        opcao = menu()
        
        if opcao == "7":
            print("👋 Obrigado por usar a calculadora!")
            break
        elif opcao == "6":
            try:
                num = float(input("Digite um número: "))
                resultado = raiz_quadrada(num)
                print(f"√{num} = {resultado}")
            except ValueError:
                print("❌ Erro: Digite um número válido!")
        elif opcao in ["1", "2", "3", "4", "5"]:
            num1, num2 = obter_numeros()
            if num1 is not None and num2 is not None:
                if opcao == "1":
                    resultado = soma(num1, num2)
                    print(f"{num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtracao(num1, num2)
                    print(f"{num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicacao(num1, num2)
                    print(f"{num1} × {num2} = {resultado}")
                elif opcao == "4":
                    resultado = divisao(num1, num2)
                    print(f"{num1} ÷ {num2} = {resultado}")
                elif opcao == "5":
                    resultado = potenciacao(num1, num2)
                    print(f"{num1} ^ {num2} = {resultado}")
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
```

### **🎯 Requisitos:**
- ✅ **Funções bem definidas** com docstrings
- ✅ **Tratamento de erros** com try/except
- ✅ **Menu interativo** com loop while
- ✅ **Validação de entrada** do usuário
- ✅ **Interface amigável** com mensagens claras

---

## 🎯 Exercício 3: Desafio Bônus - Jogo da Velha

### **Objetivo:**
Criar um jogo da velha completo que demonstre **domínio avançado** de Python básico.

### **Especificações:**
- Tabuleiro 3x3
- Alternância entre jogadores (X e O)
- Validação de jogadas
- Verificação de vitória/empate
- Interface clara e intuitiva

### **💡 Dicas para o Desafio:**
- Use **listas** para representar o tabuleiro
- Implemente **funções** para cada ação
- Use **estruturas de controle** para validação
- Crie uma **interface visual** clara

---

## 📊 Critérios de Avaliação

### **✅ Excelente (9-10 pontos):**
- Código bem estruturado e comentado
- Todas as funcionalidades implementadas
- Tratamento de erros adequado
- Interface amigável e intuitiva

### **✅ Bom (7-8 pontos):**
- Código funcional com pequenos problemas
- Maioria das funcionalidades implementadas
- Alguns tratamentos de erro
- Interface básica mas funcional

### **⚠️ Regular (5-6 pontos):**
- Código funciona mas com problemas
- Funcionalidades básicas implementadas
- Pouco tratamento de erro
- Interface básica

---

## 🚀 Próximos Passos

Após completar estes exercícios, você estará pronto para:
- 🧠 **Machine Learning** com Scikit-learn
- 📊 **Análise de dados** com Pandas
- 🌐 **Desenvolvimento web** com Flask
- 🤖 **Automação** e scripts avançados

---

> **🎉 Parabéns! Você completou a base sólida em Python e está pronto para projetos de IA!**

---

*Próximo submódulo: Vamos explorar Machine Learning e algoritmos de IA!*
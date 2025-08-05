# 🔄 O que é Recursão?

Recursão é quando uma função chama a si mesma. É como uma função que se repete até chegar a um ponto de parada.

## 📝 Comparação de Formatação

### ❌ Formatação sem recursão (loop normal):
```python
for i in range(len(lista)):
    print(f"   - {lista[i]}")
```

### ✅ Formatação com recursão:
```python
def print_recursivo(lista, indice=0):
    if indice >= len(lista):
        return  # Ponto de parada
    print(f"   - {lista[i]}")
    print_recursivo(lista, indice + 1)  # Chama a si mesma
```

## 🎯 Como funciona:

```python
pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 35}
]

# Com recursão
def print_pessoas_recursivo(lista, indice=0):
    if indice >= len(lista):
        return  # Ponto de parada
    pessoa = lista[indice]
    print(f"   - {pessoa['nome']}, {pessoa['idade']} anos")
    print_pessoas_recursivo(lista, indice + 1)  # Recursão

# Sem recursão (loop normal)
for pessoa in pessoas:
    print(f"   - {pessoa['nome']}, {pessoa['idade']} anos")
```

## 🔧 Vantagens da Recursão:

- ✅ **Código elegante** - Lógica mais limpa
- ✅ **Controle total** - Você decide quando parar
- ✅ **Flexibilidade** - Pode adicionar lógica personalizada
- ✅ **Indentação dinâmica** - Pode criar hierarquias visuais

## 📊 Exemplos práticos:

### Lista simples:
```python
frutas = ["maçã", "banana", "laranja"]

def print_frutas_recursivo(lista, indice=0):
    if indice >= len(lista):
        return
    print(f"   - {lista[indice]}")
    print_frutas_recursivo(lista, indice + 1)
```

### Lista de dicionários:
```python
pessoas = [
    {"nome": "Ana", "idade": 25, "cidade": "SP"},
    {"nome": "Bob", "idade": 30, "cidade": "RJ"},
    {"nome": "Carlos", "idade": 35, "cidade": "MG"}
]

def print_pessoas_detalhado(lista, indice=0):
    if indice >= len(lista):
        return
    pessoa = lista[indice]
    print(f"   - {pessoa['nome']} ({pessoa['idade']} anos) - {pessoa['cidade']}")
    print_pessoas_detalhado(lista, indice + 1)
```

### Recursão com nível (indentação):
```python
def print_com_nivel(lista, nivel=0):
    if not lista:
        return
    indentacao = "   " * nivel
    print(f"{indentacao}- {lista[0]}")
    print_com_nivel(lista[1:], nivel)
```

---

Recursão é basicamente uma função que diz: *"Ei, processa um item e depois chama a si mesma para o próximo!"* 🔄

---

# 💡 Dicas Rápidas

## 🔤 Testando códigos direto no terminal

Uma forma rápida de executar um trecho de código direto no terminal:

### ✅ Forma correta (uma linha):
```bash
python3 -c "hora = 14; minuto = 30; print(f'São {hora:02d}:{minuto:02d}')"
```

### ✅ Forma correta (múltiplas linhas):
```bash
python3 -c "
hora = 14
minuto = 30
print(f'São {hora:02d}:{minuto:02d}')
"
```

### ❌ Forma incorreta (causa erro):
```bash
python3 -c "hora = 14
minuto = 30
print(f"São {hora:02d}:{minuto:02d}")"
```

## 🎯 Dicas importantes:

- ✅ **Use ponto e vírgula** (`;`) para separar comandos em uma linha
- ✅ **Use aspas simples** (`'`) dentro de f-strings no terminal
- ✅ **Use aspas duplas** (`"`) para envolver todo o código
- ❌ **Evite quebras de linha** sem escape adequado

## 📊 Exemplos práticos:

### Testando f-strings:
```bash
python3 -c "nome = 'Maria'; idade = 25; print(f'Olá {nome}, você tem {idade} anos')"
```

### Testando listas:
```bash
python3 -c "frutas = ['maçã', 'banana']; print(f'Fruta: {frutas[0]}')"
```

### Testando dicionários:
```bash
python3 -c "pessoa = {'nome': 'João', 'idade': 30}; print(f'{pessoa[\"nome\"]} tem {pessoa[\"idade\"]} anos')"
```

---

**Dica:** Use o terminal para testar rapidamente pequenos trechos de código antes de criar arquivos! ⚡
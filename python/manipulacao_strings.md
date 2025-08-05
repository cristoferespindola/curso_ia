# 🔤 Manipulação de Strings

## 📝 O que é o f-string?

O `f` é a **f-string** (formatted string literal) do Python. É uma forma moderna e elegante de formatar strings.

### ❌ Formatação antiga (sem f):
```python
print("   - " + str(resultado))
print("   - {}".format(resultado))
print("   - %s" % resultado)
```

### ✅ Formatação moderna (com f):
```python
print(f"   - {resultado}")
```

## 🎯 Como funciona:

```python
nome = "João"
idade = 25

# Com f-string
print(f"Olá {nome}, você tem {idade} anos")
# Saída: Olá João, você tem 25 anos

# Sem f-string (mais verboso)
print("Olá {}, você tem {} anos".format(nome, idade))
print("Olá " + nome + ", você tem " + str(idade) + " anos")
```

## 🔧 Vantagens do f-string:

- ✅ **Mais legível** - Código mais limpo
- ✅ **Mais rápido** - Performance melhor
- ✅ **Menos erros** - Sintaxe mais simples
- ✅ **Expressões diretas** - Pode usar variáveis e expressões dentro de `{}`

## 📊 Exemplos práticos:

### Variáveis simples:
```python
nome = "Maria"
print(f"Olá {nome}")
```

### Expressões matemáticas:
```python
x = 10
y = 5
print(f"Soma: {x + y}")
```

### Formatação de números:
```python
preco = 19.99
print(f"Preço: R$ {preco:.2f}")
```

### Múltiplas variáveis:
```python
hora = 14
minuto = 30
print(f"São {hora:02d}:{minuto:02d}")
```

## 🔤 Formatadores de String

### O que é `02d`?

#### Decomposição:
- `0` = **preenchimento** (com zeros)
- `2` = **largura** (2 caracteres)
- `d` = **tipo** (decimal/inteiro)

#### Como funciona:
```python
hora = 14
minuto = 30

# Com formatador 02d
print(f"São {hora:02d}:{minuto:02d}")  # São 14:30

# Sem formatador
print(f"São {hora}:{minuto}")           # São 14:30

# Exemplo com números menores
hora = 9
minuto = 5

print(f"São {hora:02d}:{minuto:02d}")  # São 09:05  ← Aqui vemos a diferença!
print(f"São {hora}:{minuto}")           # São 9:5    ← Sem formatação
```

### Outros exemplos de formatadores:

#### Para números inteiros:
```python
numero = 5

print(f"{numero:02d}")    # 05    (2 dígitos, preenchido com 0)
print(f"{numero:3d}")     #   5   (3 dígitos, preenchido com espaço)
print(f"{numero:03d}")    # 005   (3 dígitos, preenchido com 0)
```

#### Para números decimais:
```python
preco = 19.99

print(f"R$ {preco:.2f}")    # R$ 19.99    (2 casas decimais)
print(f"R$ {preco:.1f}")    # R$ 20.0     (1 casa decimal)
print(f"R$ {preco:6.2f}")   # R$  19.99   (6 caracteres, 2 decimais)
```

## 🎯 Por que usar `02d` para horários?

✅ **Consistência visual** - Sempre 2 dígitos  
✅ **Formato padrão** - 09:05 em vez de 9:5  
✅ **Legibilidade** - Mais fácil de ler  
✅ **Padrão internacional** - Formato HH:MM  

## 📝 Resumo dos formatadores:

| Formatador | Exemplo | Resultado | Descrição |
|------------|---------|-----------|-----------|
| `02d` | `f"{5:02d}"` | `05` | 2 dígitos, preenchido com 0 |
| `3d` | `f"{5:3d}"` | `  5` | 3 dígitos, preenchido com espaço |
| `.2f` | `f"{19.99:.2f}"` | `19.99` | 2 casas decimais |
| `6.2f` | `f"{19.99:6.2f}"` | ` 19.99` | 6 caracteres, 2 decimais |

---

O `f` é basicamente um atalho que diz ao Python: *"Ei, dentro das chaves `{}` coloca o valor das variáveis!"* 🚀 
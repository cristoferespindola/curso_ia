# 🐍 Python - Complete Guide

Welcome to the complete Python guide! Here you will find tips, concepts, and practical examples organized by topics.

## 🌍 Language / Idioma

- 🇺🇸 **[English](#index)** (Current)
- 🇧🇷 **[Português](README.md)** (Original version)

## 📚 Index

### 🚀 **Initial Setup**
- 🐍 [Python Installation](../modulo-1/submodulo-1A/aula%201A.1/instalacao_python.md)
- 🐍 [Creating a Virtual Environment](../modulo-1/submodulo-1A/aula%201A.3/criando_ambiente_virtual.md)
- 🧱 [Basic Structure of a Python Script](../modulo-1/submodulo-1A/aula%201A.4/estrura_basica.md)

### 🔤 **Data Manipulation**
- 🔤 [String Manipulation](./manipulacao_strings.md)
  - F-strings and modern formatting
  - String formatters (`02d`, `.2f`, etc.)
  - Practical formatting examples
  - Formatter table

### 📊 **Essential Libraries**
- 🐼 [Pandas](./pandas.md)
  - Data manipulation and analysis
  - DataFrames and Series
  - Data cleaning and transformation
  - Machine Learning integration

- 🧠 [Scikit-learn](./sklearn.md)
  - Supervised Machine Learning
  - Classification and regression
  - Main models (LogisticRegression, RandomForest, etc.)
  - Evaluation and metrics

### 🔄 **Advanced Concepts**
- 🔄 [Fundamental Concepts](./conceitos.md)
  - Recursion and functions
  - Quick terminal tips
  - Inline code testing
  - Practical examples

## 🚀 How to use this guide

1. **Start with setup** - Install Python and configure your environment
2. **Learn the basics** - Script structure and string manipulation
3. **Explore libraries** - Pandas for data, Scikit-learn for ML
4. **Practice** - Use the terminal to test quickly

## 💡 Quick Tips

### Testing code in terminal:
```bash
python3 -c "print('Hello, Python!')"
```

### Formatting strings:
```python
name = "Maria"
age = 25
print(f"Hello {name}, you are {age} years old")
```

### Formatting time:
```python
hour = 9
minute = 5
print(f"It's {hour:02d}:{minute:02d}")  # It's 09:05
```

### Using Pandas:
```python
import pandas as pd
df = pd.DataFrame({'column': [1, 2, 3]})
print(df.head())
```

### Using Scikit-learn:
```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
print("Model created!")
```

## 📖 File structure

```
python/
├── README.md                    # ← This file (main menu)
├── manipulacao_strings.md       # F-strings and formatting
├── pandas.md                   # Data manipulation
├── sklearn.md                  # Machine Learning
└── conceitos.md               # Recursion and tips

modulo-1/submodulo-1A/
├── aula 1A.1/
│   └── instalacao_python.md    # Python installation
├── aula 1A.3/
│   └── criando_ambiente_virtual.md # Virtual environments
└── aula 1A.4/
    └── estrura_basica.md       # Script structure
```

## 🎯 Next steps

- [x] ✅ Initial setup (Python + venv)
- [x] ✅ Basic script structure
- [x] ✅ String manipulation
- [x] ✅ Pandas for data
- [x] ✅ Scikit-learn for ML
- [x] ✅ Recursion concepts
- [ ] 📝 Add more Python topics
- [ ] 📝 Create practical exercises
- [ ] 📝 Add advanced examples
- [ ] 📝 Include performance tips

## 🔗 Useful Links

- [🐍 Python.org](https://www.python.org/) - Official website
- [📚 Python Documentation](https://docs.python.org/) - Official documentation
- [🐼 Pandas Documentation](https://pandas.pydata.org/) - Pandas guide
- [🧠 Scikit-learn Documentation](https://scikit-learn.org/) - Scikit-learn guide
- [🎓 Real Python](https://realpython.com/) - Excellent tutorials

---

**Tip:** Use `Ctrl+F` (or `Cmd+F`) to quickly search in files! 🔍

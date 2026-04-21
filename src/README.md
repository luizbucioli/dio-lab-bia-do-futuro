# Passo a Passo de Execução

## Setup do Ollama
```bash
# 1. Instalar Ollama (Ollama.com)
# 2. Baixar um modelo leve
ollama run llama3-groq-tool-use:8b

# 3. Testar se funciona ollama
ollama run llama3-groq-tool-use:8b "Olá!"
```

## Código completo

Todo o código-fonte está no arquivo `app.py`

## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 3. Rodar o app
streamlit run ./src/app.py
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```

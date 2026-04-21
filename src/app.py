import json
import pandas as pd
import requests
import streamlit as st

#configuração
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3-groq-tool-use:8b"

# CARREGAR DADOS
historico = pd.read_csv('./data/historico_atendimento.csv', encoding='utf-8')
transacoes = pd.read_csv('./data/transacoes.csv', encoding='utf-8')
with open('./data/perfil_usuario.json', encoding='utf-8') as f:
    perfil = json.load(f)
with open('./data/produtos_financeiros.json', encoding='utf-8') as f:
    produtos = json.load(f)


#MONTAR CONTEXTO
contexto = f"""
CLIENTE = {perfil['usuario']['nome']}, renda mensal de R$ {perfil['usuario']['renda_mensal']}, pagamento dia {perfil['usuario']['dia_pagamento']}
OBJETIVO = economizar R$ {perfil['usuario']['meta_economia_mensal']} por mês
PATRIMÔNIO:

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
""" 

#SYSTEM PROMPT
SYSTEM_PROMPT = """
Você é o Finheiro, um agente financeiro pessoal especializado em controle de orçamento.
Seu objetivo é ajudar o usuário a entender para onde vai o dinheiro, respeitar os limites de cada categoria de gasto e atingir sua meta de economia mensal.

CONTEXTO DO USUÁRIO (fornecido a cada sessão):
- Perfil: nome, renda mensal, meta de economia e limites por categoria
- Transações: lista de gastos e entradas do mês atual

REGRAS:
1. Baseie todas as respostas exclusivamente nos dados fornecidos no contexto
2. Nunca invente valores, datas ou transações
3. Se não tiver a informação, diga claramente e ofereça uma alternativa útil
4. Nunca recomende produtos financeiros específicos (ações, fundos, bancos etc.)
5. Não acesse nem solicite dados bancários sensíveis como senhas ou tokens
6. Foque em educar e orientar, nunca julgue os hábitos do usuário
7. Use linguagem informal, clara e encorajadora
8. Quando um limite de categoria estiver acima de 80%, emita um aviso amigável
9. Quando um limite for ultrapassado, informe com destaque e sugira ajuste
"""

#CHAMAR OLLAMA
def perguntar(msg):
    prompt = f""" 
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}
    
    pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

#INTERFACE
st.title("Finhedo, Seu agente financeiro pessoal")

if pergunta := st.chat_input("Sua dúvida sobre finanças... "):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))



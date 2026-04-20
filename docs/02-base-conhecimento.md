# Base de Conhecimento
 
## Dados Utilizados
 
| Arquivo | Formato | Para que Serve no Finheiro? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Armazena interações anteriores do usuário com o agente, permitindo que o Finheiro entenda padrões de dúvidas e personalize as respostas com base no histórico de conversa. |
| `perfil_usuario.json` | JSON | Contém o perfil financeiro do usuário (renda mensal, limites por categoria, meta de economia e dia de pagamento), usado para contextualizar alertas e sugestões de forma personalizada. |
| `produtos_financeiros.json` | JSON | Lista de categorias de gastos com percentuais recomendados e exemplos de despesas, usado para comparar os gastos reais do usuário com parâmetros saudáveis baseados na regra 50-30-20. |
| `transacoes.csv` | CSV | Registro de todas as transações financeiras do usuário (data, descrição, categoria, valor, tipo), principal fonte de dados para análise de orçamento, alertas e relatórios mensais. |
 
---
 
## Adaptações nos Dados
 
> Você modificou ou expandiu os dados mockados? Descreva aqui.
 
Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade
```
HISTORICO DE ATENDIMENTO DO CLIENTE (data/historico_atendimento.csv):
id,data,usuario,mensagem_usuario,resposta_agente,intencao
1,2026-04-01,ana_costa,Quanto gastei esse mês até agora?,"Até agora você gastou R$ 320.50 em Alimentação e R$ 45.00 em Transporte. Quer ver o resumo completo por categoria?",consulta_resumo
2,2026-04-05,ana_costa,Estou gastando muito com streaming?,"Você tem R$ 55.90 com Netflix registrado este mês. Seu limite para Assinaturas é R$ 150 — ainda está dentro! Quer que eu te avise quando chegar perto do limite?",consulta_categoria
3,2026-04-10,ana_costa,Adiciona uma compra na farmácia de 80 reais,Anotado! Registrei R$ 80.00 em Saúde (Farmácia). Seu total em Saúde este mês ficou em R$ 80.00.,registro_transacao
4,2026-04-16,ana_costa,Recebi meu salário hoje de 4200 reais,Ótimo! Registrei sua entrada de R$ 4.200.00. Vamos planejar o mês? Posso mostrar como distribuir com base nos seus limites de categoria.,registro_entrada
5,2026-04-20,ana_costa,Quanto ainda posso gastar em alimentação?,"Você já gastou R$ 615.50 em Alimentação. Seu limite é R$ 800 — ainda tem R$ 184.50 disponíveis. Cuidado para não ultrapassar até o fim do mês!",consulta_limite
6,2026-04-28,ana_costa,Fui ao bar e gastei 95 reais,Registrado! R$ 95.00 em Lazer (Bar). Você já usou R$ 140.00 do seu limite de R$ 300 em Lazer este mês.,registro_transacao
7,2026-04-30,ana_costa,Consegui guardar os 600 reais esse mês!,"Parabéns! Você atingiu sua meta de economia mensal de R$ 600.00. Continue assim!",meta_atingida


DADOS DO CLIENTE E PERFIL (data/perfil_usuario.json):
{
  "usuario": {
    "id": "ana_costa",
    "nome": "Ana Costa",
    "renda_mensal": 4200,
    "meta_economia_mensal": 600,
    "dia_pagamento": 15
  },
  "limites_por_categoria": {
    "Alimentação": 800,
    "Transporte": 400,
    "Lazer": 300,
    "Assinaturas": 150,
    "Saúde": 300,
    "Moradia": 500,
    "Vestuário": 200,
    "Poupança": 600
  },
  "alertas": {
    "percentual_aviso": 80,
    "notificar_ao_ultrapassar": true
  }
}

PRODUTOS FINANCEIROS DO CLIENTE (data/produtos_financeiros.json):
{
  "categorias_orcamento": [
    {
      "categoria": "Alimentação",
      "descricao": "Supermercado, restaurantes, delivery, padaria e similares.",
      "percentual_recomendado": 20,
      "exemplos": [
        "Supermercado",
        "iFood",
        "Restaurante",
        "Padaria",
        "Feira"
      ]
    },
    {
      "categoria": "Moradia",
      "descricao": "Aluguel, condomínio, água, luz, internet e gás.",
      "percentual_recomendado": 30,
      "exemplos": [
        "Aluguel",
        "Conta de Luz",
        "Conta de Água",
        "Internet",
        "Gás"
      ]
    },
    {
      "categoria": "Transporte",
      "descricao": "Combustível, transporte público, aplicativos de mobilidade.",
      "percentual_recomendado": 10,
      "exemplos": [
        "Uber",
        "Gasolina",
        "Ônibus",
        "Metrô",
        "99"
      ]
    },
    {
      "categoria": "Saúde",
      "descricao": "Plano de saúde, farmácia, consultas e academia.",
      "percentual_recomendado": 10,
      "exemplos": [
        "Farmácia",
        "Consulta médica",
        "Academia",
        "Plano de saúde"
      ]
    },
    {
      "categoria": "Lazer",
      "descricao": "Cinema, bares, viagens e entretenimento em geral.",
      "percentual_recomendado": 10,
      "exemplos": [
        "Cinema",
        "Bar",
        "Show",
        "Viagem"
      ]
    },
    {
      "categoria": "Assinaturas",
      "descricao": "Serviços de streaming e assinaturas recorrentes.",
      "percentual_recomendado": 5,
      "exemplos": [
        "Netflix",
        "Spotify",
        "Amazon Prime",
        "Disney+"
      ]
    },
    {
      "categoria": "Vestuário",
      "descricao": "Roupas, calçados e acessórios.",
      "percentual_recomendado": 5,
      "exemplos": [
        "Loja de Roupas",
        "Calçados",
        "Acessórios"
      ]
    },
    {
      "categoria": "Poupança",
      "descricao": "Reserva de emergência e metas financeiras.",
      "percentual_recomendado": 10,
      "exemplos": [
        "Transferência para reserva",
        "Investimento",
        "CDB"
      ]
    }
  ],
  "regra_base": "50-30-20",
  "descricao_regra": "50% para necessidades (moradia, alimentação, transporte), 30% para desejos (lazer, vestuário, assinaturas), 20% para poupança e metas."
}

TRANSACOES DO CLIENTES (data/transacoes.csv):
id,data,descricao,categoria,valor,tipo
1,2026-04-01,Supermercado Extra,Alimentação,320.50,saida
2,2026-04-03,Uber,Transporte,45.00,saida
3,2026-04-05,Netflix,Assinaturas,55.90,saida
4,2026-04-08,Restaurante Sabor & Arte,Alimentação,110.00,saida
5,2026-04-10,Farmácia Drogasil,Saúde,80.00,saida
6,2026-04-12,Academia SmartFit,Saúde,99.90,saida
7,2026-04-14,Posto de Gasolina,Transporte,150.00,saida
8,2026-04-15,Salário,Renda,4200.00,entrada
9,2026-04-16,iFood,Alimentação,62.00,saida
10,2026-04-18,Spotify,Assinaturas,21.90,saida
11,2026-04-19,Ônibus mensal,Transporte,110.00,saida
12,2026-04-20,Padaria do Bairro,Alimentação,35.00,saida
13,2026-04-22,Cinema,Lazer,45.00,saida
14,2026-04-23,Loja de Roupas,Vestuário,180.00,saida
15,2026-04-25,Conta de Luz,Moradia,210.00,saida
16,2026-04-25,Conta de Internet,Moradia,99.90,saida
17,2026-04-26,Mercadinho local,Alimentação,88.00,saida
18,2026-04-28,Bar com amigos,Lazer,95.00,saida
19,2026-04-29,Consulta médica,Saúde,150.00,saida
20,2026-04-30,Transferência reserva,Poupança,600.00,saida
```
 
---
 
## Estratégia de Integração
 
### Como os dados são carregados?
 
```python
import json
import pandas as pd

# CARREGAR DADOS
historicos = pd.read_csv(open('./data/historico_atendimento.csv'))
transacoes = pd.read_csv(open('./data/transacoes.csv'))
perfil = json.load(open('./data/perfil_usuario.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))
```
 
### Como os dados são usados no prompt?
 
Os dados vão no **system prompt**, formatados como um bloco de contexto estruturado. As transações mais recentes (últimos 30 dias) são incluídas dinamicamente a cada sessão, enquanto o perfil do usuário e os limites por categoria ficam fixos no prompt base. Isso permite que o agente compare os gastos atuais com os limites definidos e gere alertas sem precisar de consultas externas durante a conversa.
 
---
 
## Exemplo de Contexto Montado
 
> Mostre um exemplo de como os dados são formatados para o agente.
 
```
Dados do Usuário:
- Nome: Ana Costa
- Renda mensal: R$ 4.200,00
- Meta de economia mensal: R$ 600,00
- Limites por categoria:
  - Alimentação: R$ 800,00
  - Transporte: R$ 400,00
  - Lazer: R$ 300,00
  - Assinaturas: R$ 150,00
  - Saúde: R$ 300,00
 
Gastos do mês atual (abril/2026):
- 01/04: Supermercado Extra (Alimentação) - R$ 320,50
- 03/04: Uber (Transporte) - R$ 45,00
- 05/04: Netflix (Assinaturas) - R$ 55,90
- 08/04: Restaurante (Alimentação) - R$ 110,00
- 10/04: Farmácia Drogasil (Saúde) - R$ 80,00
...
 
Resumo atual:
- Alimentação: R$ 615,50 de R$ 800,00 (77% do limite) 
- Transporte: R$ 305,00 de R$ 400,00 (76% do limite) 
- Assinaturas: R$ 77,80 de R$ 150,00 (52% do limite)
- Saúde: R$ 329,90 de R$ 300,00 (110% do limite) 
- Lazer: R$ 140,00 de R$ 300,00 (47% do limite)
```

# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que Serve no Finheiro? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | [Sua descrição aqui] |
| `perfil_investidor.json` | JSON | [Sua descrição aqui] |
| `produtos_financeiros.json` | JSON | [Sua descrição aqui] |
| `transacoes.csv` | CSV | [Sua descrição aqui] |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

```python
  import pandas as pd
  import json

  # CSVs
  historicos = pd.read_csv('data/historico_atendimento.csv')
  transacoes = pd.read_csv('data/transacoes.csv')

  #JSON
  with open('data/perfil_investidor.json', 'r', enconding='utf-8') as f:
      perfil = json.load(f)

with open('data/produto_financeiros.json', 'r', enconding='utf-8') as f:
      produtos = json.load(f)

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```

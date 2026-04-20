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
 
Sim. O arquivo `transacoes.csv` foi expandido para incluir as colunas `categoria` (ex: Alimentação, Transporte, Lazer) e `tipo` (`entrada` ou `saida`), permitindo ao Finheiro agrupar gastos por categoria, calcular saldos e emitir alertas de limite. O `perfil_investidor.json` foi renomeado para `perfil_usuario.json` e adaptado para refletir informações de orçamento pessoal, incluindo os campos `renda_mensal`, `limites_por_categoria`, `meta_economia_mensal` e configurações de alertas. O `produtos_financeiros.json` foi expandido com percentuais recomendados por categoria baseados na regra 50-30-20 e exemplos de despesas para facilitar a categorização automática.
 
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

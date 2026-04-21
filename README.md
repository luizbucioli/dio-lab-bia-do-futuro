# 💰 Finhedo — Agente de Controle de Orçamento Pessoal

> Projeto desenvolvido como solução do Lab **"BIA do Futuro"** na [DIO](https://www.dio.me/), com foco em agentes financeiros inteligentes com IA Generativa.

---

## 🤖 O que é o Finhedo?

**Finhedo** é um agente conversacional de controle de orçamento pessoal. Ele analisa o histórico financeiro do usuário, identifica padrões de gasto e oferece orientações proativas e personalizadas — indo além do simples registro de transações.

---

## 🗂️ Estrutura do Repositório

```
dio-lab-bia-do-futuro/
│
├── data/                          # Dados mockados do agente
│   ├── historico_atendimento.csv  # Histórico de interações
│   ├── perfil_investidor.json     # Perfil financeiro do usuário
│   ├── produtos_financeiros.json  # Produtos e categorias disponíveis
│   └── transacoes.csv             # Histórico de transações
│
├── docs/                          # Documentação completa
│   ├── 01-documentacao-agente.md  # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md    # Estratégia de dados
│   ├── 03-prompts.md              # Engenharia de prompts
│   ├── 04-metricas.md             # Métricas e avaliação
│   └── 05-pitch.md                # Roteiro do pitch
│
├── src/
│   └── app.py                     # Código da aplicação
│
└── assets/                        # Imagens e diagramas
```

---

## 📋 Documentação

| Arquivo | Descrição |
|---|---|
| `01-documentacao-agente.md` | Caso de uso, persona e arquitetura do Finhedo |
| `02-base-conhecimento.md` | Estratégia de dados e base de conhecimento |
| `03-prompts.md` | System prompt e engenharia de prompts |
| `04-metricas.md` | Métricas de avaliação e anti-alucinação |
| `05-pitch.md` | Roteiro de apresentação do agente |

---

## ⚙️ Principais Funcionalidades

- **Análise de gastos** com base no histórico de transações
- **Alertas proativos** quando categorias de gasto ultrapassam o limite
- **Sugestões personalizadas** de economia e organização financeira
- **Perfil do investidor** para recomendações contextualizadas
- **Anti-alucinação**: respostas seguras, baseadas apenas nos dados fornecidos

---

## 🚀 Como Executar

```bash
# Clone o repositório
git clone https://github.com/luizbucioli/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# Instale as dependências
pip install -r requirements.txt

# Execute o agente
python src/app.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Python** — lógica do agente
- **IA Generativa** — motor conversacional
- **CSV / JSON** — dados mockados estruturados

---

## 👤 Autor

Desenvolvido por **Luiz Bucioli** como entrega do desafio BIA do Futuro — DIO.

[![GitHub](https://img.shields.io/badge/GitHub-luizbucioli-181717?logo=github)](https://github.com/luizbucioli)

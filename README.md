# 📊 Sistema Integrado de Gestão: Inventário de Riscos Ocupacionais (NR-1)

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicação web desenvolvida em **Python** e **Streamlit** para automação, controle operacional e conformidade regulatória em **Segurança e Saúde no Trabalho (SST)**, com foco estrito nas diretrizes da **NR-1 (Gerenciamento de Riscos Ocupacionais - GRO)**, Ergonomia (**AEP**) e Análise de Riscos Psicossociais (**ARP**).

---

## 🖥️ Demonstração Visual das Telas

* **Painel de Controle Unificado (Início):** Visão geral do ecossistema e navegação integrada entre os módulos de inventário e saúde ocupacional.
* **Módulo de Inventário e Ativos:** Controle operacional de equipamentos, coletores de dados, terminais e mobiliário ergonômico com filtros dinâmicos e exportação de relatórios em CSV.
* **Dashboard Gerencial de Riscos (NR-1, AEP e ARP):** Painel executivo com matriz de calor de riscos ocupacionais, indicadores de dias afastados (CID) e taxa de adesão ao questionário COPSOQ.

---

## 🚀 Funcionalidades Principais

* **Gestão de Riscos (NR-1 / NRO):** Matriz de calor automatizada cruzando Severidade x Probabilidade.
* **Ergonomia (AEP) e Psicossocial (ARP):** Monitoramento de postos de trabalho e indicadores de saúde mental.
* **Inventário de Ativos Operacionais:** Listagem com rastreabilidade de equipamentos de TI, terminais de caixa e suprimentos.
* **Exportação de Dados:** Recursos de download direto de bases filtradas em formato CSV.

---

## 📂 Estrutura do Repositório

```text
inventario-riscos-nr1-streamlit/
├── app.py                  # Página principal (Dashboard Unificado)
├── pages/                  # Módulos independentes do Streamlit
│   ├── 1_Inventario.py     # Gestão de ativos e equipamentos
│   └── 2_Dashboard_Riscos.py # Indicadores e Matriz de Riscos (NR-1)
├── data/                   # Bases de dados locais (CSV)
│   └── inventario_base.csv
├── modules/                # Regras de negócio e lógica de suporte
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação oficial

🌐 Consulta On-line
Aplicação em Produção: Disponível em breve na Streamlit Community Cloud.

👤 Autor
Desenvolvido por Marcos Silva

Profissional focado em inovação operacional, análise de dados aplicada e transição para a Gestão de Pessoas e SST.

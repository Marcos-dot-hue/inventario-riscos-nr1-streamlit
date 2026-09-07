# 📊 Sistema Integrado de Gestão: Inventário de Riscos Ocupacionais (NR-1)

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicação web desenvolvida em **Python** e **Streamlit** para automação, controle operacional e conformidade regulatória em **Segurança e Saúde no Trabalho (SST)**, com foco estrito nas diretrizes da **NR-1 (Gerenciamento de Riscos Ocupacionais - GRO)**, Ergonomia (**AEP**) e Análise de Riscos Psicossociais (**ARP**)[cite: 1].

---

## 🖥️ Demonstração Visual das Telas

### 1. Painel de Controle Unificado (Início)
Visão geral do ecossistema e navegação integrada entre os módulos de inventário e saúde ocupacional[cite: 1].

### 2. Módulo de Inventário e Ativos
Controle operacional de equipamentos, coletores de dados, terminais e mobiliário ergonômico com filtros dinâmicos e exportação de relatórios em CSV[cite: 1].

### 3. Dashboard Gerencial de Riscos (NR-1, AEP e ARP)
Painel executivo com matriz de calor de riscos ocupacionais, indicadores de dias afastados (CID) e taxa de adesão ao questionário COPSOQ[cite: 1].

---

## 🚀 Funcionalidades Principais

* **Gestão de Riscos (NR-1 / NRO):** Matriz de calor automatizada cruzando Severidade x Probabilidade[cite: 1].
* **Ergonomia (AEP) e Psicossocial (ARP):** Monitoramento de postos de trabalho e indicadores de saúde mental[cite: 1].
* **Inventário de Ativos Operacionais:** Listagem com rastreabilidade de equipamentos de TI, terminais de caixa e suprimentos[cite: 1].
* **Exportação de Dados:** Recursos de download direto de bases filtradas em formato CSV[cite: 1].

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
```[cite: 1]

---

## 🛠️ Como Executar Localmente

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Marcos-dot-hue/inventario-riscos-nr1-streamlit.git](https://github.com/Marcos-dot-hue/inventario-riscos-nr1-streamlit.git)
   cd inventario-riscos-nr1-streamlit
   ```[cite: 1]

2. **Crie e ative um ambiente virtual (venv):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```[cite: 1]

3. **Instale as dependências:**
   ```bash
   pip# Sistema Integrado de Gestão: Inventário de Riscos Ocupacionais (NR-1)

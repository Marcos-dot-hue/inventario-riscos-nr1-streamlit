import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventário | Sistema Integrado", page_icon="📦", layout="wide")

st.title("📦 Módulo de Inventário e Ativos")
st.subheader("Controle de Equipamentos, Suprimentos e Ativos Operacionais")

st.markdown("""
Este módulo gerencia o inventário físico da operação, integrando o controle de ativos com a conformidade de segurança.
""")

st.divider()

# Dados de inventário
data = {
    "Código": ["EQ-001", "EQ-002", "EQ-003", "SUP-101", "SUP-102"],
    "Item / Descrição": ["Coletor de Dados Zebra TC26", "Terminal POS / Caixa", "Cadeira Ergonômica Operacional", "Bobina Térmica 80x40", "Etiqueta Térmica Adesiva"],
    "Categoria": ["Equipamento TI", "Equipamento Operacional", "Mobiliário / AEP", "Suprimento", "Suprimento"],
    "Quantidade": [45, 12, 180, 500, 1200],
    "Status": ["Disponível", "Em Uso", "Conforme NR-1", "Estoque Adequado", "Estoque Baixo"]
}

df_inventario = pd.DataFrame(data)

# Filtros na barra lateral
st.sidebar.header("Filtros do Inventário")
categoria_filtro = st.sidebar.selectbox("Filtrar por Categoria", ["Todas"] + list(df_inventario["Categoria"].unique()))

if categoria_filtro != "Todas":
    df_exibicao = df_inventario[df_inventario["Categoria"] == categoria_filtro]
else:
    df_exibicao = df_inventario

# Exibição dos dados
st.dataframe(df_exibicao, use_container_width=True)

# Botão de Download em CSV
csv_data = df_exibicao.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Baixar Dados Filtrados em CSV",
    data=csv_data,
    file_name="inventario_exportado.csv",
    mime="text/csv",
)

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Total de Itens Cadastrados", len(df_inventario))
col2.metric("Categorias Ativas", df_inventario["Categoria"].nunique())
col3.metric("Itens Críticos / Baixos", len(df_inventario[df_inventario["Status"] == "Estoque Baixo"]))

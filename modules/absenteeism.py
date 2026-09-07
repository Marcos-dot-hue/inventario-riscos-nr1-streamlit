import streamlit as st
import pandas as pd
import plotly.express as px

def render_absenteeism_chart(df_absenteeism: pd.DataFrame):
    st.subheader("2. Afastamentos Médicos (Grupos CID: M e F)")
    filtered_df = df_absenteeism[df_absenteeism["grupo_cid"].isin(["M", "F"])].copy()
    col1, col2 = st.columns(2)
    
    with col1:
        group_summary = filtered_df.groupby("grupo_nome")["dias_afastamento"].sum().reset_index()
        fig_bar = px.bar(
            group_summary, x="grupo_nome", y="dias_afastamento", color="grupo_nome",
            color_discrete_map={
                "Grupo M (Osteomuscular / AEP)": "#3498DB",
                "Grupo F (Mental e Comportamental / ARP)": "#9B59B6"
            },
            labels={"dias_afastamento": "Total Dias Afastados", "grupo_nome": "Grupo CID"},
            text_auto=True
        )
        fig_bar.update_layout(showlegend=False, height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        cid_summary = filtered_df.groupby(["cid", "descricao", "grupo_cid"])["quantidade_casos"].sum().reset_index().sort_values(by="quantidade_casos", ascending=True).tail(8)
        fig_cid = px.bar(
            cid_summary, x="quantidade_casos", y="cid", orientation="h", color="grupo_cid",
            color_discrete_map={"M": "#3498DB", "F": "#9B59B6"},
            hover_data=["descricao"], labels={"quantidade_casos": "Nº Casos", "cid": "Código CID"},
            text_auto=True
        )
        fig_cid.update_layout(height=350, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_cid, use_container_width=True)

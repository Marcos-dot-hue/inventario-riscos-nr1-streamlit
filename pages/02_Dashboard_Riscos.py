import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Dashboard de Riscos | NR-1, AEP e ARP", layout="wide")

@st.cache_data
def load_data():
    df_risks = pd.DataFrame([
        {"id": 1, "perigo": "Esforço repetitivo", "probabilidade": 4, "severidade": 3},
        {"id": 2, "perigo": "Sobrecarga mental", "probabilidade": 5, "severidade": 4},
        {"id": 3, "perigo": "Postura estática prolongada", "probabilidade": 3, "severidade": 2},
        {"id": 4, "perigo": "Clima organizacional tóxico", "probabilidade": 2, "severidade": 5},
        {"id": 5, "perigo": "Iluminação deficiente", "probabilidade": 2, "severidade": 1},
        {"id": 6, "perigo": "Trabalho em turnos desfavoráveis", "probabilidade": 3, "severidade": 3},
    ])
    df_absenteeism = pd.DataFrame([
        {"cid": "M54.5", "descricao": "Dor lombar baixa", "grupo_cid": "M", "grupo_nome": "Grupo M (Osteomuscular / AEP)", "dias_afastamento": 180, "quantidade_casos": 12},
        {"cid": "M65.8", "descricao": "Outras sinovites e tenossinovites", "grupo_cid": "M", "grupo_nome": "Grupo M (Osteomuscular / AEP)", "dias_afastamento": 120, "quantidade_casos": 8},
        {"cid": "F32", "descricao": "Episódios depressivos", "grupo_cid": "F", "grupo_nome": "Grupo F (Mental e Comportamental / ARP)", "dias_afastamento": 250, "quantidade_casos": 6},
        {"cid": "F43.1", "descricao": "Estado de 'stress' pós-traumático / Burnout", "grupo_cid": "F", "grupo_nome": "Grupo F (Mental e Comportamental / ARP)", "dias_afastamento": 210, "quantidade_casos": 7},
    ])
    df_copsoq = pd.DataFrame([
        {"setor": "Operações / Produção", "total_elegiveis": 150, "respondentes": 120},
        {"setor": "Administrativo / Finanças", "total_elegiveis": 40, "respondentes": 36},
        {"setor": "Logística", "total_elegiveis": 60, "respondentes": 32},
        {"setor": "Atendimento ao Cliente", "total_elegiveis": 50, "respondentes": 45},
    ])
    return df_risks, df_absenteeism, df_copsoq

def render_risk_matrix(df_risks):
    st.subheader("1. Matriz de Risco Ocupacional (NR-1 / NRO)")
    matrix_values = [[s * p for p in range(1, 6)] for s in range(1, 6)]
    counts = [[0] * 5 for _ in range(5)]
    for _, row in df_risks.iterrows():
        p, s = int(row["probabilidade"]), int(row["severidade"])
        if 1 <= p <= 5 and 1 <= s <= 5:
            counts[s - 1][p - 1] += 1
    
    cell_text = [
        [f"NRO {matrix_values[s][p]}<br><b>({counts[s][p]} riscos)</b>" for p in range(5)]
        for s in range(5)
    ]
    discrete_colors = [
        [0.0, "#2ECC71"], [0.25, "#2ECC71"],
        [0.26, "#F1C40F"], [0.50, "#F1C40F"],
        [0.51, "#E74C3C"], [1.0, "#E74C3C"]
    ]
    fig = go.Figure(data=go.Heatmap(
        z=matrix_values,
        x=["P1 - Muito Baixa", "P2 - Baixa", "P3 - Média", "P4 - Alta", "P5 - Muito Alta"],
        y=["S1 - Leve", "S2 - Menor", "S3 - Moderada", "S4 - Grave", "S5 - Catastrófica"],
        text=cell_text,
        texttemplate="%{text}",
        hoverongaps=False,
        colorscale=discrete_colors,
        showscale=False
    ))
    fig.update_layout(xaxis_title="Probabilidade", yaxis_title="Severidade", height=450, margin=dict(l=40, r=40, t=30, b=40))
    st.plotly_chart(fig, use_container_width=True)

def render_absenteeism_chart(df_absenteeism):
    st.subheader("2. Afastamentos Médicos (Grupos CID: M e F)")
    filtered_df = df_absenteeism[df_absenteeism["grupo_cid"].isin(["M", "F"])].copy()
    col1, col2 = st.columns(2)
    with col1:
        group_summary = filtered_df.groupby("grupo_nome")["dias_afastamento"].sum().reset_index()
        fig_bar = px.bar(
            group_summary, x="grupo_nome", y="dias_afastamento", color="grupo_nome",
            color_discrete_map={"Grupo M (Osteomuscular / AEP)": "#3498DB", "Grupo F (Mental e Comportamental / ARP)": "#9B59B6"},
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

def render_copsoq_rate(df_copsoq):
    st.subheader("3. Taxa de Adesão à Pesquisa COPSOQ (ARP)")
    total_elegiveis = df_copsoq["total_elegiveis"].sum()
    total_respondentes = df_copsoq["respondentes"].sum()
    taxa_global = (total_respondentes / total_elegiveis * 100) if total_elegiveis > 0 else 0
    col1, col2 = st.columns([1, 2])
    with col1:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=taxa_global, number={"suffix": "%"},
            title={"text": "Adesão Global"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2ECC71" if taxa_global >= 70 else "#F39C12"},
                "steps": [{"range": [0, 50], "color": "#FADBD8"}, {"range": [50, 70], "color": "#FCF3CF"}, {"range": [70, 100], "color": "#D4EFDF"}]
            }
        ))
        fig_gauge.update_layout(height=320, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)
    with col2:
        df_copsoq["taxa_setor"] = (df_copsoq["respondentes"] / df_copsoq["total_elegiveis"]) * 100
        fig_dept = px.bar(
            df_copsoq, x="taxa_setor", y="setor", orientation="h",
            labels={"taxa_setor": "Adesão (%)", "setor": "Setor / Área"},
            text=df_copsoq["taxa_setor"].apply(lambda x: f"{x:.1f}%")
        )
        fig_dept.add_vline(x=70, line_dash="dash", line_color="red", annotation_text="Meta (70%)")
        fig_dept.update_layout(height=320, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig_dept, use_container_width=True)

def main():
    st.title("Dashboard Gerencial: Gestão de Riscos (NR-1, AEP e ARP)")
    st.caption("Visão executiva integrada de Ergonomia (AEP), Psicossocial (ARP) e Saúde Ocupacional")
    df_risks, df_absenteeism, df_copsoq = load_data()
    
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total de Perigos Identificados", len(df_risks))
    kpi2.metric("Total Dias Afastados (CID M + F)", int(df_absenteeism["dias_afastamento"].sum()))
    taxa_adesao = (df_copsoq["respondentes"].sum() / df_copsoq["total_elegiveis"].sum()) * 100
    kpi3.metric("Taxa de Adesão COPSOQ", f"{taxa_adesao:.1f}%")
    
    st.divider()
    render_risk_matrix(df_risks)
    st.divider()
    render_absenteeism_chart(df_absenteeism)
    st.divider()
    render_copsoq_rate(df_copsoq)

if __name__ == "__main__":
    main()

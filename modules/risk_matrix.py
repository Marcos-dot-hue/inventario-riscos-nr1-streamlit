import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_risk_matrix(df_risks: pd.DataFrame):
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
    
    fig.update_layout(
        xaxis_title="Probabilidade",
        yaxis_title="Severidade",
        height=450,
        margin=dict(l=40, r=40, t=30, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)

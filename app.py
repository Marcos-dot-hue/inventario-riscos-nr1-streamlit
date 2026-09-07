import streamlit as st

st.set_page_config(
    page_title="Sistema Integrado | Inventário & Riscos",
    page_icon="🛡️",
    layout="wide"
)

st.title("Sistema de Gestão Integrada")
st.subheader("Painel de Controle Unificado — Operação e Conformidade")

st.markdown("""
Este ambiente consolida as ferramentas de gestão da operação. Utilize o **menu de navegação na barra lateral esquerda** para alternar entre os módulos:

* **📦 Inventário:** Controle de ativos, equipamentos, suprimentos e histórico de inventário físico.
* **📊 Dashboard de Riscos:** Monitoramento executivo integrado de Ergonomia (**AEP**), Psicossocial (**ARP**) e Saúde Ocupacional (**NR-1**).
""")

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.info("💡 **Dica de Navegação:** As páginas operam de forma independente, compartilhando a mesma base de dados e o ecossistema do agente.")
with col2:
    st.success("🚀 **Status do Sistema:** Ambiente virtual (`venv`) ativo e módulos sincronizados com sucesso.")

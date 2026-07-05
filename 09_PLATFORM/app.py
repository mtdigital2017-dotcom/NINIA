
import streamlit as st

st.set_page_config(
    page_title="NINIA",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ N I N I A")

st.caption("Conocimiento que protege")

st.divider()

pregunta = st.text_input(
    "¿Qué deseas investigar hoy?"
)

if st.button("Investigar"):

    st.success("Próximamente este botón ejecutará el Research Engine.")

st.divider()

st.subheader("Estado del proyecto")

st.write("✅ Plataforma iniciada")

st.write("✅ Research Engine integrado")

st.write("🚧 Knowledge Package")

st.write("🚧 Observatorio")

st.write("🚧 NINIA Media")

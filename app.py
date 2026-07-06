
import streamlit as st

st.set_page_config(
    page_title="NINIA",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ NINIA")
st.subheader("Conocimiento que protege")

st.write(
    """
Bienvenido a la primera versión de NINIA.

Esta plataforma transformará documentos, investigaciones y evidencia
en conocimiento útil para la protección integral de niñas, niños
y adolescentes en entornos digitales.
"""
)

pregunta = st.text_input(
    "¿Qué deseas investigar hoy?"
)

if st.button("Investigar"):

    st.success("Pregunta recibida")

    st.write("Tu pregunta fue:")

    st.write(pregunta)

st.divider()

st.markdown("## Próximamente")

st.write("📚 Observatorio Mundial")

st.write("📰 NINIA Media")

st.write("🧠 Knowledge Package")

st.write("📊 Decision Canvas")

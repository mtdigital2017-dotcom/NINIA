
import streamlit as st
from components.layout import render_layout

render_layout("Sala de Investigación")

# ===========================
# SIDEBAR
# ===========================

with st.sidebar:

    st.title("🔎 NINIA")

    st.markdown("---")

    st.button("Nueva investigación", use_container_width=True)

    st.markdown("### Historial")

    st.write("• Ciberacoso")
    st.write("• IA Generativa")
    st.write("• Grooming")
    st.write("• Alfabetización Mediática")

# ===========================
# CABECERA
# ===========================

st.title("🔎 Sala de Investigación")

st.caption(
    "Realiza investigaciones utilizando el motor de conocimiento de NINIA."
)

st.divider()

# ===========================
# CONSULTA
# ===========================

pregunta = st.text_area(
    "¿Qué deseas investigar?",
    placeholder="Ejemplo: ¿Qué evidencia existe sobre ciberacoso en América Latina?",
    height=140
)

col1, col2, col3 = st.columns([1,1,5])

with col1:
    investigar = st.button("Investigar")

with col2:
    limpiar = st.button("Limpiar")

st.divider()

# ===========================
# RESULTADOS
# ===========================

st.subheader("Resultados")

if investigar:

    st.success("Aquí se conectará el Research Engine.")

else:

    st.info("Escribe una consulta para comenzar.")

st.divider()

st.subheader("Fuentes")

st.empty()

st.subheader("Documentos")

st.empty()

st.subheader("Referencias")

st.empty()

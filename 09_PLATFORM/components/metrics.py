
import streamlit as st

def metrics():

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🌍 Países", "196")

    with c2:
        st.metric("📚 Fuentes", "2.540")

    with c3:
        st.metric("📄 Papers", "56.812")

    with c4:
        st.metric("🛰 Observatorio", "24/7")


import streamlit as st
from pathlib import Path

BASE = Path("/content/drive/MyDrive/NINIA/09_PLATFORM")

st.set_page_config(
    page_title="NINIA",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css = ""

for archivo in [
    "base.css",
    "layout.css",
    "home.css"
]:

    ruta = BASE/"styles"/archivo

    if ruta.exists():
        css += ruta.read_text(encoding="utf-8")

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

from ui.home import render_home

render_home()

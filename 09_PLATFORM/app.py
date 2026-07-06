
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent

html = (BASE/"frontend"/"index.html").read_text(encoding="utf-8")
css = (BASE/"frontend"/"css"/"theme.css").read_text(encoding="utf-8")
js = (BASE/"frontend"/"js"/"app.js").read_text(encoding="utf-8")

html = html.replace("</head>",f"<style>{css}</style></head>")
html = html.replace("</body>",f"<script>{js}</script></body>")

st.set_page_config(
    page_title="NINIA",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

components.html(
    html,
    height=2500,
    scrolling=True
)

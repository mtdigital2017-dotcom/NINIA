
import streamlit as st
from pathlib import Path

from components.navbar import navbar
from components.hero import hero
from components.metrics import metrics

st.set_page_config(
    page_title="NINIA",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css = Path("styles/theme.css")

if css.exists():
    st.markdown(
        f"<style>{css.read_text()}</style>",
        unsafe_allow_html=True
    )

st.markdown("""

<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

.block-container{

padding-top:0rem;
padding-left:0rem;
padding-right:0rem;
padding-bottom:3rem;

max-width:100%;

}

</style>

""",unsafe_allow_html=True)

navbar()

hero()

metrics()



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

css = Path(__file__).parent / "styles" / "theme.css"

if css.exists():
    st.markdown(
        f"<style>{css.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

[data-testid="stHeader"]{
display:none;
}

[data-testid="stToolbar"]{
display:none;
}

[data-testid="stSidebar"]{
display:none;
}

.block-container{
padding-top:0rem !important;
padding-bottom:0rem !important;
padding-left:0rem !important;
padding-right:0rem !important;
max-width:100% !important;
}

div[data-testid="stVerticalBlock"]{
padding-top:0rem;
}

</style>
""",unsafe_allow_html=True)

navbar()

hero()

st.markdown("<div style='height:40px'></div>",unsafe_allow_html=True)

metrics()


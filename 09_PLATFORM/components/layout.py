
import streamlit as st

def render_layout(page_title="NINIA"):

    st.set_page_config(
        page_title=page_title,
        page_icon="🌍",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
<style>

#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}

[data-testid="stSidebar"]{
display:none;
}

.block-container{
padding:0rem !important;
max-width:100% !important;
}

</style>
""", unsafe_allow_html=True)


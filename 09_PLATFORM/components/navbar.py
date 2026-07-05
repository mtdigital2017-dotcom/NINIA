
import streamlit as st

def navbar():

    st.markdown("""

<div class="topbar">

    <div class="logo-area">

        <div class="logo-title">
            NINIA
        </div>

        <div class="logo-sub">
            Conocimiento que protege
        </div>

    </div>

    <div class="menu">

        <a class="active">Inicio</a>

        <a>Observatorio</a>

        <a>Investigar</a>

        <a>Biblioteca</a>

        <a>Comparar</a>

        <a>Tendencias</a>

        <a>Media</a>

        <a>Studio</a>

        <a>Academy</a>

    </div>

    <div class="actions">

        <input
        class="search"
        placeholder="Buscar en NINIA..."
        >

        <div class="bell">
        🔔
        </div>

        <div class="avatar">
        JM
        </div>

    </div>

</div>

<div class="navbar-space"></div>

""",unsafe_allow_html=True)

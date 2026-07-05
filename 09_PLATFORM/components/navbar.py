
import streamlit as st

def navbar():

    st.markdown("""

<div class="topbar">

<div class="logo">

<div class="logo-main">
NINIA
</div>

<div class="logo-sub">
Knowledge Intelligence Platform
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

<a>Academy</a>

</div>

<div class="right">

<input placeholder="Buscar..." />

<div class="avatar">
JM
</div>

</div>

</div>

<div class="spacer"></div>

""",unsafe_allow_html=True)

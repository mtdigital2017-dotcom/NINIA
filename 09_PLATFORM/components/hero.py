
import streamlit as st

def hero():

    st.markdown("""

<div class="hero">

<div class="hero-left">

<div class="hero-badge">
Plataforma Mundial de Inteligencia
</div>

<h1>

Inteligencia mundial<br>
para proteger<br>
lo que más importa.

</h1>

<p>

Investigación • Regulación • IA • Evidencia

</p>

<div class="hero-buttons">

<button class="btn-primary">
Investigar
</button>

<button class="btn-secondary">
Explorar
</button>

</div>

</div>

<div class="hero-right">

<div class="search-box">

<h3>
¿Qué deseas investigar?
</h3>

<input placeholder="Escribe una pregunta..." />

<button>
Buscar
</button>

</div>

</div>

</div>

""",unsafe_allow_html=True)

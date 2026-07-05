
import streamlit as st

def hero():

    st.markdown("""

<section class="hero">

<div class="hero-left">

<div class="badge">

INTELIGENCIA • INVESTIGACIÓN • EVIDENCIA

</div>

<h1>

Inteligencia mundial
para proteger
lo que más importa.

</h1>

<p>

Investigamos.
Analizamos.
Comunicamos.
Transformamos evidencia en conocimiento accionable.

</p>

</div>

<div class="hero-right">

<div class="search-card">

<h3>

¿Qué deseas investigar hoy?

</h3>

<input
placeholder="Ej. Protección digital infantil, IA generativa, grooming..." />

<button>

Investigar

</button>

</div>

</div>

</section>

""",unsafe_allow_html=True)

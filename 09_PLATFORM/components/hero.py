
import streamlit as st

def hero():

    st.markdown("""

<section class="hero">

<div class="hero-left">

<div class="hero-badge">
🌍 Plataforma Mundial de Inteligencia
</div>

<h1>

Inteligencia mundial<br>
para proteger<br>
lo que más importa.

</h1>

<p>

Investigamos políticas públicas.<br>
Analizamos evidencia científica.<br>
Transformamos información en decisiones.

</p>

<div class="hero-search">

<input
placeholder="¿Qué deseas investigar hoy?"
>

<button>

Investigar

</button>

</div>

<div class="hero-actions">

<button>

Observatorio

</button>

<button>

Knowledge Packages

</button>

<button>

Academy

</button>

</div>

</div>

<div class="hero-right">

<div class="feature-card">

<div class="feature-tag">

DESTACADO

</div>

<h2>

Reducir el ciberacoso requiere la participación activa de las familias.

</h2>

<p>

Síntesis de evidencia basada en estudios internacionales.

</p>

<div class="feature-footer">

🌎 38 países · 📄 412 estudios

</div>

</div>

</div>

</section>

""",unsafe_allow_html=True)


import streamlit as st

def render_home():

    st.markdown("""

<div class="page">

<div class="topbar">

<div class="brand">

<div class="logo">
NINIA
</div>

<div class="subtitle">
Conocimiento que protege
</div>

</div>

<div class="menu">

<a class="active">Inicio</a>

<a>Observatorio</a>

<a>Investigación</a>

<a>Biblioteca</a>

<a>Tendencias</a>

<a>Academy</a>

</div>

<div class="actions">

<input placeholder="Buscar..." />

<div class="avatar">
JM
</div>

</div>

</div>


<section class="hero">

<div class="hero-left">

<div class="badge">

PLATAFORMA MUNDIAL

</div>

<h1>

Inteligencia mundial<br>
para proteger<br>
a niñas, niños y adolescentes

</h1>

<p>

La primera plataforma que integra inteligencia artificial,
investigación, regulación y cooperación internacional
para proteger la niñez en entornos digitales.

</p>

<div class="buttons">

<button class="primary">

Comenzar investigación

</button>

<button class="secondary">

Explorar

</button>

</div>

</div>

<div class="hero-right">

<div class="hero-card">

<h2>

¿Qué deseas investigar?

</h2>

<input
placeholder="Ejemplo: Grooming, TikTok, IA..."
>

<button>

Buscar

</button>

</div>

</div>

</section>

</div>

""", unsafe_allow_html=True)

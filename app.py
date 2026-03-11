import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página en Streamlit
# Esto define cómo se ve la pestaña en el navegador
st.set_page_config(
    page_title="Presentación Ejecutiva", 
    page_icon="🏢",
    layout="centered"
)

# 2. Ocultar la interfaz predeterminada de Streamlit
# Esto elimina el menú superior y la marca de agua inferior para que parezca una app web pura
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* Quitamos el padding por defecto para usar todo el espacio */
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Código HTML, CSS y JS de la presentación móvil (Totalmente Anónimo)
html_mobile = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="viewport" content="width=device-width, initial-scale=1.0">
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600&display=swap');

    :root {
        --primary: #0A192F; 
        --accent: #D32F2F; 
        --bg-color: #F8F9FA;
    }

    body, html {
        margin: 0; padding: 0; height: 100%; width: 100%;
        font-family: 'Inter', sans-serif; 
        background-color: transparent; /* Fondo transparente para integrar con Streamlit */
        display: flex; justify-content: center; align-items: center;
    }

    /* Contenedor formato 9:16 móvil */
    #mobile-deck {
        width: 400px; height: 710px; 
        background-color: var(--bg-color);
        position: relative; overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border-radius: 8px;
    }

    .slide {
        width: 100%; height: 100%;
        position: absolute; top: 0; left: 0;
        opacity: 0; transition: opacity 0.3s ease;
        padding: 40px 30px; box-sizing: border-box;
        display: flex; flex-direction: column; justify-content: center;
        pointer-events: none;
    }
    .slide.active { opacity: 1; pointer-events: auto; }

    h1 { font-family: 'Playfair Display', serif; color: var(--primary); font-size: 34px; line-height: 1.2; margin: 0 0 20px 0; }
    h2 { font-size: 22px; color: var(--accent); margin: 0 0 10px 0; }
    p { font-size: 18px; color: #444; line-height: 1.5; margin-bottom: 20px; }

    .service-card {
        background: white; padding: 15px; border-radius: 8px;
        border-left: 4px solid var(--primary); margin-bottom: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .service-card h3 { margin: 0 0 5px 0; font-size: 18px; color: var(--primary); }
    .service-card p { margin: 0; font-size: 14px; }

    .stat { text-align: center; margin-bottom: 25px; }
    .stat-num { font-family: 'Playfair Display'; font-size: 48px; font-weight: bold; color: var(--accent); }
    .stat-text { font-size: 16px; font-weight: 600; color: var(--primary); }

    /* Controles táctiles */
    .touch-area {
        position: absolute; top: 0; height: 100%; width: 50%; z-index: 10; cursor: pointer;
    }
    .touch-left { left: 0; }
    .touch-right { right: 0; }
    
    .progress {
        position: absolute; bottom: 20px; left: 0; width: 100%;
        display: flex; justify-content: center; gap: 8px; z-index: 20;
    }
    .dot { width: 8px; height: 8px; background: #CCC; border-radius: 50%; }
    .dot.active { background: var(--primary); }
</style>
</head>
<body>

<div id="mobile-deck">
    
    <div class="touch-area touch-left" onclick="move(-1)"></div>
    <div class="touch-area touch-right" onclick="move(1)"></div>

    <div class="slide active" id="m-slide-1">
        <h2 style="font-size: 20px; color: var(--primary); font-family: 'Playfair Display', serif;">CONSULTING<span style="color: var(--accent);">GROUP</span></h2>
        <h1 style="font-size: 42px;">Más allá del<br>cumplimiento.</h1>
        <p>Inteligencia legal y predictiva para blindar el patrimonio de su empresa.</p>
        <div style="margin-top: auto; font-size: 12px; color: #888; text-align: center;">Toca el lado derecho para avanzar 👉</div>
    </div>

    <div class="slide" id="m-slide-2">
        <h2>El Riesgo Actual</h2>
        <h1>Anticipar o Pagar.</h1>
        <p>La complejidad fiscal y regulatoria no perdona improvisaciones.</p>
        <div class="service-card" style="border-left-color: var(--accent);">
            <h3>El problema</h3>
            <p>Reaccionar a multas y requerimientos frena el crecimiento corporativo.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-3">
        <h2>La Solución</h2>
        <h1>Estrategia Data-Driven</h1>
        <p>Análisis avanzado para modelar escenarios regulatorios.</p>
        <ul style="padding-left: 20px; font-size: 18px; color: #444; line-height: 1.6;">
            <li>Cero sorpresas fiscales.</li>
            <li>Continuidad operativa garantizada.</li>
            <li>Protección patrimonial proactiva.</li>
        </ul>
    </div>

    <div class="slide" id="m-slide-4">
        <h2>Estructura</h2>
        <h1>Ecosistema Integral</h1>
        <div class="service-card">
            <h3>Estrategia Fiscal</h3>
            <p>Optimización inteligente de carga tributaria.</p>
        </div>
        <div class="service-card">
            <h3>Gestión Regulatoria</h3>
            <p>Aseguramos cumplimiento sin pausas operativas.</p>
        </div>
        <div class="service-card">
            <h3>Blindaje Patrimonial</h3>
            <p>Protegemos el legado y capital de los socios.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-5">
        <h2>Impacto</h2>
        <h1>Resultados Medibles</h1>
        <div class="stat">
            <div class="stat-num">98%</div>
            <div class="stat-text">Mitigación de Riesgo Fiscal</div>
        </div>
        <div class="stat">
            <div class="stat-num">100%</div>
            <div class="stat-text">Continuidad Operativa</div>
        </div>
    </div>

    <div class="slide" id="m-slide-6" style="background: var(--primary); color: white;">
        <h2 style="color: var(--accent);">Siguiente Paso</h2>
        <h1 style="color: white;">Diagnóstico Inicial</h1>
        <p style="color: #DDD;">Evalúe su estructura corporativa actual sin compromiso.</p>
        
        <div style="background: white; border-radius: 8px; padding: 20px; margin-top: 30px; text-align: center; position: relative; z-index: 30;">
            <h3 style="color: var(--primary); margin: 0 0 10px 0;">Contáctenos</h3>
            <p style="color: #444; font-size: 16px; margin: 0; font-weight: 600;">✉️ contacto@consultinggroup.com</p>
            <p style="color: #444; font-size: 16px; margin: 5px 0 0 0;">📞 [Código] 0000 0000</p>
        </div>
    </div>

    <div class="progress" id="dots">
        <div class="dot active"></div><div class="dot"></div><div class="dot"></div>
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
    </div>
</div>

<script>
    let curr = 1;
    const tot = 6;
    const dotsContainer = document.getElementById('dots');

    function move(step) {
        document.getElementById('m-slide-' + curr).classList.remove('active');
        dotsContainer.children[curr-1].classList.remove('active');
        
        curr += step;
        if (curr > tot) curr = 1;
        if (curr < 1) curr = tot;
        
        document.getElementById('m-slide-' + curr).classList.add('active');
        dotsContainer.children[curr-1].classList.add('active');
    }
</script>

</body>
</html>
"""

# 4. Renderizar el HTML dentro de Streamlit
# Ajustamos la altura para asegurarnos de que el contenedor de 710px quepa sin barras de desplazamiento
components.html(html_mobile, height=750, scrolling=False)

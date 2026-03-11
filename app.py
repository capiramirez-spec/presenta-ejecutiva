import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página en Streamlit
st.set_page_config(
    page_title="Presentación Ejecutiva", 
    page_icon="🏢",
    layout="centered"
)

# 2. Ocultar la interfaz predeterminada de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Código HTML, CSS y JS de la presentación móvil (8 páginas - Anónimo)
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
        background-color: transparent; 
        display: flex; justify-content: center; align-items: center;
    }

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
    h2 { font-size: 20px; color: var(--accent); margin: 0 0 10px 0; letter-spacing: 1px; text-transform: uppercase;}
    p { font-size: 17px; color: #444; line-height: 1.5; margin-bottom: 20px; }

    .service-card {
        background: white; padding: 18px; border-radius: 8px;
        border-left: 4px solid var(--primary); margin-bottom: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    .service-card h3 { margin: 0 0 8px 0; font-size: 19px; color: var(--primary); }
    .service-card p { margin: 0; font-size: 15px; color: #555;}

    .stat { text-align: center; margin-bottom: 25px; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);}
    .stat-num { font-family: 'Playfair Display'; font-size: 44px; font-weight: bold; color: var(--accent); line-height: 1; }
    .stat-text { font-size: 15px; font-weight: 600; color: var(--primary); margin-top: 5px; }

    /* Controles táctiles */
    .touch-area { position: absolute; top: 0; height: 100%; width: 50%; z-index: 10; cursor: pointer; }
    .touch-left { left: 0; }
    .touch-right { right: 0; }
    
    .progress {
        position: absolute; bottom: 20px; left: 0; width: 100%;
        display: flex; justify-content: center; gap: 6px; z-index: 20;
    }
    .dot { width: 7px; height: 7px; background: #CCC; border-radius: 50%; transition: background 0.3s;}
    .dot.active { background: var(--primary); width: 20px; border-radius: 4px;}
</style>
</head>
<body>

<div id="mobile-deck">
    
    <div class="touch-area touch-left" onclick="move(-1)"></div>
    <div class="touch-area touch-right" onclick="move(1)"></div>

    <div class="slide active" id="m-slide-1">
        <div style="font-size: 16px; color: var(--primary); font-family: 'Playfair Display', serif; font-weight: bold; margin-bottom: 30px;">
            CONSULTING<span style="color: var(--accent);">GROUP</span>
        </div>
        <h1 style="font-size: 42px;">Más allá del<br>cumplimiento.</h1>
        <p style="font-size: 19px;">Inteligencia legal y predictiva para blindar el patrimonio de su empresa.</p>
        <div style="margin-top: auto; font-size: 13px; color: #888; text-align: center; font-weight: 600;">Toca la derecha para avanzar 👉</div>
    </div>

    <div class="slide" id="m-slide-2">
        <h2>El Riesgo Actual</h2>
        <h1>Anticipar o Pagar.</h1>
        <p>La complejidad fiscal y regulatoria no perdona improvisaciones en empresas en crecimiento.</p>
        <div class="service-card" style="border-left-color: var(--accent);">
            <h3 style="color: var(--accent);">El costo de reaccionar</h3>
            <p>Apagar incendios con multas o bloqueos operativos destruye márgenes y frena la escalabilidad.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-3">
        <h2>El Paradigma</h2>
        <h1>Certeza en lugar de miedo.</h1>
        <p>Hacer las cosas "bien" es el estándar. Nuestro valor es transformar la incertidumbre normativa en una ventaja competitiva.</p>
        <div class="service-card">
            <h3>Nuestro Enfoque</h3>
            <p>No esperamos el requerimiento de la autoridad; estructuramos su empresa para que ese requerimiento jamás proceda.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-4">
        <h2>Metodología</h2>
        <h1>Decisiones Data-Driven</h1>
        <p>Implementamos tecnología analítica y modelos predictivos poco comunes en el sector legal tradicional.</p>
        <ul style="padding-left: 20px; font-size: 16px; color: #444; line-height: 1.7;">
            <li><strong>Auditoría Algorítmica:</strong> Detectamos fisuras antes que la autoridad.</li>
            <li><strong>Proyección de Escenarios:</strong> Simulamos impactos fiscales.</li>
            <li><strong>Ejecución Quirúrgica:</strong> Implementamos la defensa.</li>
        </ul>
    </div>

    <div class="slide" id="m-slide-5">
        <h2>Ecosistema I</h2>
        <h1>Blindaje Operativo</h1>
        <p>Aseguramos que el día a día de su empresa fluya sin interrupciones ni fricciones institucionales.</p>
        <div class="service-card">
            <h3>Estrategia Fiscal</h3>
            <p>Optimización inteligente de la carga tributaria basada en datos y total cumplimiento legal.</p>
        </div>
        <div class="service-card">
            <h3>Gestión Regulatoria</h3>
            <p>Estructuramos contratos para garantizar la continuidad al 100% sin pausas.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-6">
        <h2>Ecosistema II</h2>
        <h1>Blindaje Estructural</h1>
        <p>Preparamos los cimientos de su corporativo para el futuro, la sucesión o la captación de capital.</p>
        <div class="service-card">
            <h3>Protección Patrimonial</h3>
            <p>Vehículos legales que aíslan y resguardan el capital personal de los socios.</p>
        </div>
        <div class="service-card">
            <h3>Arquitectura Financiera</h3>
            <p>Estructuras transparentes diseñadas para superar rigurosos procesos de Due Diligence.</p>
        </div>
    </div>

    <div class="slide" id="m-slide-7">
        <h2>Impacto</h2>
        <h1>Resultados Medibles</h1>
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <div class="stat">
                <div class="stat-num">98%</div>
                <div class="stat-text">Mitigación de Riesgo Fiscal</div>
            </div>
            <div class="stat">
                <div class="stat-num">100%</div>
                <div class="stat-text">Continuidad Operativa</div>
            </div>
        </div>
    </div>

    <div class="slide" id="m-slide-8" style="background: var(--primary); color: white;">
        <h2 style="color: var(--accent);">Siguiente Paso</h2>
        <h1 style="color: white;">Diagnóstico Inicial</h1>
        <p style="color: #DDD; font-size: 18px;">Agende una evaluación estratégica y confidencial de su estructura actual.</p>
        
        <div style="background: white; border-radius: 8px; padding: 25px 20px; margin-top: 30px; text-align: center; position: relative; z-index: 30;">
            <h3 style="color: var(--primary); margin: 0 0 15px 0; font-size: 20px;">Hablemos de negocios</h3>
            <p style="color: #444; font-size: 16px; margin: 0; font-weight: 600;">✉️ contacto@consultinggroup.com</p>
            <p style="color: #444; font-size: 16px; margin: 10px 0 0 0;">📞 [Código] 0000 0000</p>
        </div>
    </div>

    <div class="progress" id="dots">
        <div class="dot active"></div><div class="dot"></div><div class="dot"></div>
        <div class="dot"></div><div class="dot"></div><div class="dot"></div>
        <div class="dot"></div><div class="dot"></div>
    </div>
</div>

<script>
    let curr = 1;
    const tot = 8;
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

# 4. Renderizar el HTML en la aplicación web
components.html(html_mobile, height=750, scrolling=False)

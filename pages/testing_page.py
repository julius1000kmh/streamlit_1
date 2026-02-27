import streamlit as st
from datetime import date
import matplotlib.pyplot as plt
from datetime import date
import numpy as np
from datetime import datetime
st.markdown("""
    <style>
        .stApp {
            background-color: #030814;
        }

        /* Textfarbe allgemein heller machen */
        html, body, [class*="css"]  {
            color: #E6EDF3;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown(
    "<h2 style='text-align: center;'>Hey, mein Name ist Julius Schultheiß</h2>",
    unsafe_allow_html=True
)

heute  = datetime.today().date()
# ✅ Muss ganz oben stehen
import streamlit as st
import plotly.express as px
import pandas as pd












import streamlit as st
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe
            src="data:application/pdf;base64,{base64_pdf}"
            width="100%"
            height="800"
            type="application/pdf">
        </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title("PDF Viewer in Streamlit")

display_pdf("pdf.pdf")


import streamlit as st
import base64

st.title("Mein Lebenslauf")

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}"
            width="100%" 
            height="900"
            type="application/pdf">
        </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

display_pdf("pdf.pdf")











data = pd.DataFrame({
    "Datum": ["2020-01-01", "2021-06-01", "2023-03-01"],
    "Event": ["Start", "Release", "Update"],
    "Link": [
        "https://google.com",
        "https://github.com",
        "https://streamlit.io"
    ]
})

fig = px.scatter(
    data,
    x="Datum",
    y=[1, 1, 1],
    text="Event"
)

selected = st.plotly_chart(fig, use_container_width=True)

# Alternative: Events mit Buttons anzeigen
for i, row in data.iterrows():
    if st.button(row["Event"]):
        st.markdown(f"[Hier klicken]({row['Link']})")


from streamlit_timeline import timeline
import streamlit as st
import json

data = {
    "events": [
        {
            "start_date": {"year": 2020},
            "text": {
                "headline": "Projektstart",
                "text": "<a href='https://google.com' target='_blank'>Zum Projekt</a>"
            }
        },
        {
            "start_date": {"year": 2024},
            "text": {
                "headline": "Launch",
                "text": "<a href='https://github.com' target='_blank'>Mehr Infos</a>"
            }
        }
    ]
}

timeline(data, height=400)


st.write("heast oida    ")

st.markdown("### 2020 – Projektstart")
st.link_button("Zum Projekt", "https://google.com")

st.markdown("### 2023 – Launch")
st.link_button("Mehr Infos", "https://github.com")








st.write("---------------------------")

import streamlit as st
from streamlit_timeline import timeline

# 🔥 Global Dark Background
st.markdown("""
    <style>
    .stApp {
        background-color: #030814;
        color: white;
    }

    a {
        color: #030814;
        text-decoration: none;
        font-weight: 500;
    }

    a:hover {
        color: #82cfff;
    }
    </style>
""", unsafe_allow_html=True)


data = {
    "events": [
        {
            "start_date": {"year": 2020},
            "text": {
                "headline": "🚀 Projektstart",
                "text": """
                    <div style='
                        background-color:#0d1326;
                        padding:15px;
                        border-radius:12px;
                        box-shadow: 0 0 20px rgba(0,150,255,0.2);
                    '>
                        Das Projekt beginnt.<br><br>
                        <a href='https://google.com' target='_blank'>
                        🔗 Mehr erfahren
                        </a>
                    </div>
                """
            }
        },
        {
            "start_date": {"year": 2023},
            "text": {
                "headline": "✨ Launch",
                "text": """
                    <div style='
                        background-color:#0d1326;
                        padding:15px;
                        border-radius:12px;
                        box-shadow: 0 0 20px rgba(0,150,255,0.2);
                    '>
                        Offizieller Release.<br><br>
                        <a href='https://github.com' target='_blank'>
                        🔗 GitHub öffnen
                        </a>
                    </div>
                """
            }
        }
    ]
}

timeline(data, height=450)


import streamlit as st

st.markdown("""
<style>
.fade-in {
    animation: fadeIn 1.5s ease-in;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='fade-in'><h1>Hallo 🚀</h1></div>", unsafe_allow_html=True)


st.markdown("""
<style>
.glow {
    color: white;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 5px #00f; }
    to { text-shadow: 0 0 20px #00aaff; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='glow'>Neon Style</h1>", unsafe_allow_html=True)



from streamlit_lottie import st_lottie
import requests
import streamlit as st

url = "https://assets9.lottiefiles.com/packages/lf20_touohxv0.json"
lottie_json = requests.get(url).json()

st_lottie(lottie_json, height=300)


st.markdown("""
<style>
.card {
    background-color: #0d1326;
    padding: 20px;
    border-radius: 15px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0,150,255,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>Hover mich 😎</div>", unsafe_allow_html=True)



st.markdown("""
<style>
.card {
    background:#0d1326;
    padding:20px;
    border-radius:16px;
    transition: all 0.3s ease;
}
.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(0,150,255,0.25);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='card'>Hover mich 🚀</div>", unsafe_allow_html=True)



st.markdown("""
<style>
.gradient {
    background:#0d1326;
    padding:20px;
    border-radius:16px;
    position:relative;
    overflow:hidden;
}
.gradient::before {
    content:'';
    position:absolute;
    top:0;
    left:-100%;
    width:100%;
    height:100%;
    background:linear-gradient(120deg, transparent, rgba(0,150,255,0.4), transparent);
    transition:0.5s;
}
.gradient:hover::before {
    left:100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='gradient'>Shiny Effekt 💫</div>", unsafe_allow_html=True)


st.markdown("""
<style>
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    padding:20px;
    border-radius:20px;
    transition:0.3s;
}
.glass:hover {
    background: rgba(0,150,255,0.15);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='glass'>Glass Hover 🧊</div>", unsafe_allow_html=True)


st.markdown("""
<style>
.scale {
    padding:20px;
    background:#0d1326;
    border-radius:16px;
    transition:0.2s;
}
.scale:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='scale'>Pop Effekt 🔥</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.rotate {
    display:inline-block;
    padding:20px;
    background:#0d1326;
    border-radius:16px;
    transition:0.3s;
}
.rotate:hover {
    transform: rotate(2deg) scale(1.05);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='rotate'>Mini Rotation 😎</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.magnetic {
    padding:15px 30px;
    background:#001f3f;
    border-radius:30px;
    transition:0.2s;
}
.magnetic:hover {
    letter-spacing:2px;
    background:#003366;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='magnetic'>Magnetic Button</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.link-hover {
    position:relative;
    display:inline-block;
}
.link-hover::after {
    content:'';
    position:absolute;
    left:0;
    bottom:-3px;
    width:0;
    height:2px;
    background:#00aaff;
    transition:0.3s;
}
.link-hover:hover::after {
    width:100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='link-hover'>Hover Text</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.pulse:hover {
    animation:pulse 0.6s;
}
@keyframes pulse {
    0% { transform:scale(1); }
    50% { transform:scale(1.1); }
    100% { transform:scale(1); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='pulse'>Pulse Effekt 💥</div>", unsafe_allow_html=True)

st.markdown("""
<style>
.shadow-explode {
    padding:20px;
    background:#0d1326;
    border-radius:16px;
    transition:0.3s;
}
.shadow-explode:hover {
    box-shadow: 0 0 0 10px rgba(0,150,255,0.1),
                0 0 40px rgba(0,150,255,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='shadow-explode'>Explosion 💎</div>", unsafe_allow_html=True)



import streamlit as st
from streamlit_timeline import timeline

# 🔥 GLOBAL DARK THEME
st.markdown("""
<style>
/* App Background */
.stApp {
    background-color: #030814;
    color: #ffffff;
}

/* Timeline Container */
.tl-timeline {
    background-color: #030814 !important;
}

/* Main Slide Background */
.tl-slide-content-container {
    background-color: #030814 !important;
}

/* Event Card */
.tl-slide-content {
    background: linear-gradient(145deg, #0b1225, #0e1833) !important;
    border-radius: 20px !important;
    padding: 30px !important;
    box-shadow: 0 0 40px rgba(0,150,255,0.15) !important;
    color: white !important;
}

/* Headline */
.tl-headline {
    color: white !important;
}

/* Text */
.tl-text-content {
    color: #cbd5e1 !important;
}

/* Timeline Bottom Bar */
.tl-timeaxis {
    background-color: #030814 !important;
}

/* Timeline Line */
.tl-timeaxis-line {
    background-color: #00aaff !important;
}

/* Markers */
.tl-timeaxis-tick-text {
    color: #94a3b8 !important;
}

/* Navigation Arrows */
.tl-slidenav-next,
.tl-slidenav-previous {
    background-color: rgba(255,255,255,0.05) !important;
    border-radius: 50% !important;
    transition: 0.3s;
}

.tl-slidenav-next:hover,
.tl-slidenav-previous:hover {
    background-color: rgba(0,150,255,0.3) !important;
}

/* Links */
a {
    color: #00aaff !important;
    text-decoration: none;
}

a:hover {
    color: #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)


data = {
    "events": [
        {
            "start_date": {"year": 2023},
            "text": {
                "headline": "✨ LAUNCH",
                "text": """
                    Offizieller Release.<br><br>
                    <a href='https://github.com' target='_blank'>
                    🔗 GitHub öffnen
                    </a>
                """
            }
        }
    ]
}

timeline(data, height=600)




import streamlit as st
from streamlit_timeline import timeline

st.markdown("""
<style>

/* ===== APP BACKGROUND ===== */
.stApp {
    background-color: #030814;
    color: white;
}

/* ===== NAVIGATION ARROWS DARK ===== */
.tl-slidenav-next,
.tl-slidenav-previous {
    background-color: #0b1225 !important;
    border-radius: 50% !important;
    border: 1px solid rgba(255,255,255,0.08);
    transition: all 0.3s ease;
}

/* Arrow Icon selbst */
.tl-slidenav-next .tl-slidenav-icon,
.tl-slidenav-previous .tl-slidenav-icon {
    color: #ffffff !important;
    opacity: 0.9;
}

/* Hover Effekt */
.tl-slidenav-next:hover,
.tl-slidenav-previous:hover {
    background-color: #111c3a !important;
    box-shadow: 0 0 20px rgba(0,150,255,0.25);
}

/* ===== UNTERE ZEITACHSE DUNKEL ===== */
.tl-timeaxis {
    background-color: #030814 !important;
}

/* Text unten heller */
.tl-timeaxis-tick-text {
    color: #030814 !important;
}

/* ===== SLIDE TEXT HELL ===== */
.tl-headline {
    color:#030814 !important;
}

.tl-text-content {
    color: #cbd5e1 !important;
}

/* ===== TOOLTIP / PREVIEW DARK ===== */
.tl-timenav-item-content {
    background-color: #030814 !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


data = {
    "events": [
        {
            "start_date": {"year": 2023},
            "text": {
                "headline": "✨ LAUNCH",
                "text": """
                    Offizieller Release.<br><br>
                    <a href='https://github.com' target='_blank'>
                    🔗 GitHub öffnen
                    </a>
                """
            }
        }
    ]
}

timeline(data, height=600)




import streamlit as st
from streamlit_timeline import timeline

# Custom CSS für dunklen Hintergrund
st.markdown("""
    <style>
    /* Timeline Hintergrund */
    .timeline-embed {
        background-color: #030814 !important;
    }

    /* Falls der äußere Container weiß bleibt */
    .stApp {
        background-color: #030814;
    }
        .tl-timeline {
    background-color: #030814 !important;
}

.tl-slide-content {
    background-color: #030814 !important;
}
    </style>
""", unsafe_allow_html=True)

timeline(data, height=400)

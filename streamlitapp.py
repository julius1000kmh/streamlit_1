import streamlit as st
import base64
from assets.news_loader import load_news
if "notification_seen" not in st.session_state:
    st.session_state.notification_seen = False


news_items = load_news()
st.set_page_config(
    layout="wide",
    page_title="Portfolio Website Julius Schultheiß!"
)
from datetime import datetime, timedelta
col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])
# -----------------------------------
# HEADER ROW MIT BELL RECHTS
# -----------------------------------

today = datetime.today()
threshold = today - timedelta(days=10)
recent_news = [n for n in news_items if n["date"] > threshold]
unread_count = len(recent_news)

with col5:

    today = datetime.today()
    threshold = today - timedelta(days=10)
    recent_news = [n for n in news_items if n["date"] > threshold]
    unread_count = len(recent_news)

    # Wenn noch nicht gesehen → Badge anzeigen
    if not st.session_state.notification_seen and unread_count > 0:
        bell_label = f"🔔 ({unread_count})"
    else:
        bell_label = "🔔"

    with st.popover(bell_label, use_container_width=True):

        # 👉 Sobald Popover geöffnet wird → als gelesen markieren
        st.session_state.notification_seen = True

        st.markdown("### 📰 Latest News")

        sorted_news = sorted(news_items, key=lambda x: x["date"], reverse=True)

        for news in sorted_news[:5]:
            st.write(f"• {news['title']}")

        st.markdown("---")
        st.page_link("pages/news.py", label="View all News")

st.markdown("""
    <style>
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


### HEADER ROW
def round_image_hover(image_path, size=220):
    with open(image_path, "rb") as img:
        img_base64 = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    .profile-img {{
        width: {size}px;
        height: {size}px;
        border-radius: 50%;
        object-fit: cover;
        transition: transform 0.5s ease, box-shadow 0.5s ease;
        border: 0px solid #F8D7DD;
    }}

    .profile-img:hover {{
        transform: scale(1.07);
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }}
    </style>

    <div style="text-align: center;">
        <img src="data:image/png;base64,{img_base64}" class="profile-img">
    </div>
    """, unsafe_allow_html=True)
with col3:
    round_image_hover("foto.png", 220)
with col3:
    st.markdown(
        "<h1 style='text-align: center; margin-top: 0;'>HI, MY NAME IS JULIUS! 👋</h1>",
        unsafe_allow_html=True
    )

import pandas as pd
import numpy as np 
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
import webbrowser


with col3:
# Header ausblenden
    st.markdown("""
        <style>
        header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)



st.markdown(
        "<h4 style='text-align: center;'> Allow me to introduce myself: </h4>",
        unsafe_allow_html=True
    )
col1, col2, col3, col4, col5, col6 = st.columns([1, 4, 6, 6, 4, 1])

with col3:
    st.markdown("""
        I am a Mechatronics & Robotics student based in Vienna, currently taking a break 
        from my studies to gain hands-on industry experience at Mercedes-Benz. 
        During my internship, I work in Data Analysis for the electric G-Wagon.
    """)
with col4:
    st.markdown("""
        Following my internship, I am looking to continue working part-time alongside 
        my studies in a technically relevant field in or near Vienna.
    """)


### BUTTON SECTION

# ✅ Auch hier Liste verwenden!
col1, col2, col3, col4, col5, col6 = st.columns([1, 4, 6, 6, 4, 1])

with col3:
    if st.button("📁 Portfolio", use_container_width=True):
        st.switch_page("pages/Portfolio.py")

with col4:
    if st.button("📑 CV", use_container_width=True):
        st.switch_page("pages/CV.py")

with col3:
    if st.button("👨‍💼 About Me", use_container_width=True):
        st.switch_page("pages/AboutME.py")

with col4:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/Contact.py")

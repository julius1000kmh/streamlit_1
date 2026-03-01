import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Portfolio Website Julius Schultheiß!"
)

# Header ausblenden
st.markdown("""
    <style>
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


### HEADER ROW
col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])

with col1:
    if st.button("🏠", use_container_width=True):
        st.switch_page("streamlitapp.py")


with col3:
    st.markdown(
        "<h1 style='text-align: center; margin-top: 0;'>📁 Portfolio</h1>",
        unsafe_allow_html=True
    )

import streamlit as st
import base64
from assets.news_loader import load_news

news_items = load_news()
st.set_page_config(
    layout="wide",
    page_title="Portfolio Website Julius Schultheiß!"
)
from datetime import datetime, timedelta
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

with col3:
    st.markdown("## Software")
    st.warning("⚠️ Please note: All code was written manually unless otherwise specified.")
with col3:
    st.markdown("### C & C++")
col1, col2, col3, col4, col5, col6 = st.columns([1, 3,  6, 6, 3, 1])

with col3:
    if st.button("Coming soon1", use_container_width=True):
        st.switch_page("pages/portfolio.py")

with col4:
    if st.button("Coming soon2", use_container_width=True):
        st.switch_page("pages/portfolio.py")

col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])
with col3:
    st.markdown("### Python")       
col1, col2, col3, col4, col5, col6 = st.columns([1, 3,  6, 6, 3, 1])

with col3:
    if st.button("Coming soon3", use_container_width=True):
        st.switch_page("pages/portfolio.py")

with col4:
    if st.button("Coming soon4", use_container_width=True):
        st.switch_page("pages/portfolio.py")
col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])

with col3:
    st.markdown("---")
with col3:
    st.markdown("## Hardware")
with col3:
    st.markdown("### Robotics")
with col3:
    st.markdown("#### Static Robotics")
with col3:
    st.markdown("#### Aeronautical Robotics")
with col3:
    st.markdown("---")
with col3:
    st.markdown("## Research")








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
        st.switch_page("Streamlitapp.py")


with col3:
    st.markdown(
        "<h1 style='text-align: center; margin-top: 0;'>📞 Überschrift</h1>",
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
    st.markdown("""
<style>
.icon-container {
    display: flex;
    justify-content: center;
    gap: 80px;
    margin-top: 40px;
}

.icon-container a {
    color: white;
    font-size: 40px;
    text-decoration: none;
    transition: 0.3s;
}

.icon-container a:hover {
    transform: scale(1.2);
    color: #F8D7DD;
}
</style>

<link rel="stylesheet"
 href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div class="icon-container">
    <a href="mailto:julius@schultheiss-web.de">
        <i class="fas fa-envelope"></i>
    </a>
    <a href="https://www.linkedin.com/in/julius-schulthei%C3%9F-950957360/?locale=de_DE" target="_blank">
        <i class="fab fa-linkedin"></i>
    </a>
    <a href="https://github.com/julius1000kmh" target="_blank">
        <i class="fab fa-github"></i>
    </a>
</div>
""", unsafe_allow_html=True)


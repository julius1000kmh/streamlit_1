import streamlit as st
from assets.news_loader import load_news
news_items = load_news()
from datetime import datetime
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
        "<h1 style='text-align: center; margin-top: 0;'>📰 News</h1>",
        unsafe_allow_html=True
    )
        

# Neueste zuerst sortieren
sorted_news = sorted(news_items, key=lambda x: x["date"], reverse=True)
with col3:
    for news in sorted_news:
        st.markdown(f"## {news['title']}")
        st.caption(news["date"].strftime("%d.%m.%Y"))
        if "content" in news:
            st.write(news["content"])
        st.markdown("---")
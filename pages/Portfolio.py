import streamlit as st
st.set_page_config(layout="wide")

col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])

with col1:
    if st.button("🏠", use_container_width=True):
        st.switch_page("Streamlitapp.py")

with col3:
    st.markdown(
        "<h1 style='text-align: center; margin-top: 0;'>📁Portfolio</h1>",
        unsafe_allow_html=True
    )

with col3:
    st.markdown("## Software")
with col3:
    st.markdown("### C & C++")
col1, col2, col3, col4, col5, col6 = st.columns([1, 3,  6, 6, 3, 1])

with col3:
    if st.button("Chess Engine", use_container_width=True):
        st.switch_page("pages/portfolio.py")

with col4:
    if st.button("Spinning Cube", use_container_width=True):
        st.switch_page("pages/portfolio.py")

col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])
with col3:
    st.markdown("### Python")       
col1, col2, col3, col4, col5, col6 = st.columns([1, 3,  6, 6, 3, 1])

with col3:
    if st.button("Data Analysis", use_container_width=True):
        st.switch_page("pages/portfolio.py")

with col4:
    if st.button("LSTM Trading Bot", use_container_width=True):
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








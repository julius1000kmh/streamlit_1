import streamlit as st
import pandas as pd
import numpy as np 
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
import webbrowser


### SETUP
### Farbpalette: https://www.pantone.com/eu/de/artikel/color-palettes/earth-healing-farbpalette

st.markdown("""
    <style>
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.set_page_config(layout="centered",
                   page_title="Portfolio Website Julius Schultheiß!")

### INTRODUCTION

st.markdown(
    "<h1 style='text-align: center;'> HI, MY NAME IS JULIUS! </h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align: center;'> Allow me to introduce myself: </h4>",
    unsafe_allow_html=True
)
st.markdown("I am a Mechatronics & Robotics student based in Vienna, currently taking a break from my studies to gain hands-on industry experience at Mercedes-Benz. During my internship, I work in Data Analysis for the electric G-Wagon, contributing to data-driven decision-making in the context of cutting-edge electric mobility. ")
st.markdown("Following my internship, I am looking to continue working part-time alongside my studies in a technically relevant field in or near Vienna. I am particularly interested in roles at the intersection of engineering, data analysis, automation, and innovative mobility solutions, where I can apply and further develop both my technical expertise and practical experience.")

### LINKS & BUTTONS zu allen Wichtigen Infos! 

col1, col2 = st.columns(2)

with col1:
    if st.button("📁    Portfolio", use_container_width=True):
        st.switch_page("pages/portfolio.py")


with col2:
    if st.button("📑    CV", use_container_width=True):
        st.switch_page("pages/CV.py")

with col1:
    if st.button("👨‍💼 About ME", use_container_width=True):
        st.switch_page("pages/AboutME.py")


with col2:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/Contact.py")


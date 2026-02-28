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
        "<h1 style='text-align: center; margin-top: 0;'>HI, MY NAME IS JULIUS!</h1>",
        unsafe_allow_html=True
    )
        
import pandas as pd
import numpy as np 
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
import webbrowser

### My Timeline
with col3:

    st.markdown(
        "<h4 style='text-align: center;'> Timeline </h4>",
        unsafe_allow_html=True
    )

    data = pd.DataFrame([
        dict(Task="Bildung", Start="2024-10-01", Finish="2025-06-30",
             Label="BSc Mechatronics",
             Link="https://www.technikum-wien.at/studiengaenge/bachelor-mechatronik-robotik/"),

        dict(Task="Bildung", Start="2026-10-01", Finish="2028-07-01",
             Label="BSc Mechatronics",
             Link="https://www.technikum-wien.at/studiengaenge/bachelor-mechatronik-robotik/"),

        dict(Task="Praktikum", Start="2025-07-01", Finish="2026-07-01",
             Label="Mercedes-Benz G GmbH",
             Link="https://github.com"),

        dict(Task="Projekte", Start="2025-03-16", Finish="2026-03-20",
             Label="Chess Engine",
             Link="https://stackoverflow.com"),
    ])

    fig = px.timeline(
        data,
        x_start="Start",
        x_end="Finish",
        y="Task",
        text="Label",
        custom_data=["Link"],
        color_discrete_sequence=["#F8D7DD"]
    )

    fig.update_yaxes(autorange="reversed", title=None)

    fig.update_traces(
        textposition="inside",
        insidetextanchor="middle",
        textfont=dict(color="#603535", size=14),
        width=0.5
    )

    fig.update_layout(
        width=900,
        font=dict(family="Futura", size=14, color="#F8D7DD"),
        plot_bgcolor="#603535",
        paper_bgcolor="#603535",
        margin=dict(l=20, r=20, t=40, b=20)
    )

    selected_points = plotly_events(fig, click_event=True)

    if selected_points:
        point = selected_points[0]
        link = data.iloc[point["pointIndex"]]["Link"]
        webbrowser.open_new_tab(link)
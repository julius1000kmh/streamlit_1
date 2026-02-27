import streamlit as st
import pandas as pd
import numpy as np 
from datetime import date
import plotly.express as px

st.set_page_config(layout="centered")


st.markdown(
    "<h2 style='text-align: center;'>Hey, mein Name ist Julius Schultheiß</h2>",
    unsafe_allow_html=True
)

col1, col2, co3 = st.columns([1, 2, 1])

if st.button("Deutsches Menü", use_container_width=True):
    st.switch_page("pages/testing_page.py")

if st.button("English Menu", use_container_width=True):
        st.switch_page("pages/english.py")

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import date

st.set_page_config(layout="wide")

# Beispiel-Daten
data = pd.DataFrame([
    dict(Task="Analyse", Start="2026-01-01", Finish="2026-01-20", Progress=100),
    dict(Task="Implementierung", Start="2026-01-10", Finish="2026-03-01", Progress=40),
    dict(Task="Testing", Start="2026-02-15", Finish="2026-03-15", Progress=10),
])

data["Start"] = pd.to_datetime(data["Start"])
data["Finish"] = pd.to_datetime(data["Finish"])

heute = pd.to_datetime(date.today())

fig = go.Figure()

for _, row in data.iterrows():
    
    # 1️⃣ Geplante Dauer (hellgrau)
    fig.add_trace(go.Bar(
        x=[(row["Finish"] - row["Start"]).days],
        y=[row["Task"]],
        base=row["Start"],
        orientation="h",
        marker=dict(color="lightgrey"),
        showlegend=False
    ))
    
    # 2️⃣ Fortschritt berechnen
    total_days = (row["Finish"] - row["Start"]).days
    progress_days = int(total_days * row["Progress"] / 100)
    progress_end = row["Start"] + pd.Timedelta(days=progress_days)
    
    # Falls Fortschritt über heute hinausgehen würde → bei heute stoppen
    visible_end = min(progress_end, heute)
    
    if visible_end > row["Start"]:
        fig.add_trace(go.Bar(
            x=[(visible_end - row["Start"]).days],
            y=[row["Task"]],
            base=row["Start"],
            orientation="h",
            marker=dict(color="green"),
            showlegend=False
        ))

# 🔴 Heute-Linie
fig.add_vline(
    x=heute,
    line_width=2,
    line_dash="dash",
    line_color="red"
)

fig.update_layout(
    title="Gantt-Diagramm mit Fortschritt bis heute",
    barmode="overlay",
    xaxis_title="Datum",
)

fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)

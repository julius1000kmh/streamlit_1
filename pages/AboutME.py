import streamlit as st
import pandas as pd
import numpy as np 
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events
import webbrowser

st.markdown(
    "<h1 style='text-align: center;'>ABOUT ME!</h1>",
    unsafe_allow_html=True
)

st.set_page_config(layout="centered")


### My Timeline
st.markdown(
    "<h4 style='text-align: center;'> Timeline </h4>",
    unsafe_allow_html=True
)
# Beispieldaten
#data = pd.DataFrame([
 #   dict(Task="Bildung", Start="2024-10-01", Finish="2025-06-30", Link="https://www.technikum-wien.at/studiengaenge/bachelor-mechatronik-robotik/"),
  #  dict(Task="Bildung", Start="2026-10-01", Finish="2028-07-01", Link="https://www.technikum-wien.at/studiengaenge/bachelor-mechatronik-robotik/"),
   # dict(Task="MBGG", Start="2025-07-01", Finish="2026-07-01", Link="https://www.mercedes-benz-g.at"),
    #dict(Task="Projekte", Start="2025-03-16", Finish="2026-03-20", Link="https://stackoverflow.com"),
#])

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


# Gantt Diagramm
fig = px.timeline(
    data,
    x_start="Start",
    x_end="Finish",
    y="Task",
    text="Label",            # 👈 individuelle Texte
    custom_data=["Link"],
    color_discrete_sequence=["#F8D7DD"]
)

fig.update_yaxes(autorange="reversed")
fig.update_layout(
    width=900,   # ← Breite in Pixel (z.B. 900–1200 testen)
)
fig.update_yaxes(title=None)
fig.update_traces(
    textposition="inside",
    insidetextanchor="middle",
    textfont=dict(
        color="#603535",
        size=14    ),
    width=0.5
)
fig.update_layout(
    font=dict(
        family="Futura",
        size=14,
        color="#F8D7DD"   # ← Schriftfarbe
    )
)

# 🔹 Hintergrundfarbe ändern
fig.update_layout(
    plot_bgcolor="#603535",     # Bereich hinter den Balken
    paper_bgcolor="#603535"     # Gesamter Hintergrund
)


# Click Events aktivieren
selected_points = plotly_events(fig, click_event=True)

# Wenn ein Balken geklickt wurde
if selected_points:
    point = selected_points[0]
    link = data.iloc[point["pointIndex"]]["Link"]
    webbrowser.open_new_tab(link)


import streamlit as st

st.title("Hey, my name is Julius Schultheiß")

if st.button("Back to Main"):
    st.switch_page("app.py")

st.page_link("streamlitapp.py", label="🏠 Home")
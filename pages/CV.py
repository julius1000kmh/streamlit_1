import streamlit as st
st.set_page_config(layout="wide")

col1, col2, col3, col4, col5= st.columns([1, 3,  12, 3, 1])

with col1:
    if st.button("🏠", use_container_width=True):
        st.switch_page("Streamlitapp.py")

with col3:
    st.markdown(
        "<h1 style='text-align: center; margin-top: 0;'>📑 CV</h1>",
        unsafe_allow_html=True
    )

import streamlit as st
import base64

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="800px" 
            type="application/pdf">
        </iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)
with col3:
    display_pdf("CV1.pdf")








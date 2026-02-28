import streamlit as st
st.markdown(
    "<h1 style='text-align: center;'>MY CV!</h1>",
    unsafe_allow_html=True
)


# CSS für festen Button oben links
st.markdown("""
    <style>
    .home-button {
        position: fixed;
        top: 15px;
        left: 20px;
        z-index: 9999;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="home-button">', unsafe_allow_html=True)
st.page_link("streamlitapp.py", label="🏠 Home")
st.markdown('</div>', unsafe_allow_html=True)
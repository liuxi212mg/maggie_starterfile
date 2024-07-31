import streamlit as st
pip install streamlit-navigation-bar

from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)

st.title('testingmg')
st.write('Hello world!')

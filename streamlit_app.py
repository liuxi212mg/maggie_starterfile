import streamlit as st

st.title('testingmg')
st.write('Hello world!')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


# Show and update progress bar
bar = st.progress(50)
bar.progress(100)

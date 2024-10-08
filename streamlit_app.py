import streamlit as st
import pandas as pd
import numpy as np

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.title('testingmg')
st.write('Hello world!')


tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


# Show and update progress bar
bar = st.progress(50)
bar.progress(100)

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)

text_contents = '''This is some text'''
st.download_button("Download some text", text_contents)

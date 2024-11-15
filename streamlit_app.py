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


# Dropdown selection
options = ['+ Add New Option','Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an option:', options)

# Input for new options (if "Add New" is selected)
if selected_option == 'Add New Option':
    new_option = st.text_input('Enter a new option:')
    if st.button('Add'):
        if new_option:
            options.append(new_option)
            st.success(f"New option '{new_option}' added!")
        else:
            st.error("Please enter a new option.")

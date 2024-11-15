import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

# Dropdown menu with placeholder option as the first item
options = ['Select an option', '+ Add New Prompt', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an option:', options)

# Handling the placeholder behavior
if selected_option == 'Select an option':
    st.write("Please select an option above.")
elif selected_option == '+ Add New Option':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')


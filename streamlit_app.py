import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

# List of options, without the placeholder as a dropdown option
options = ['Option 1', 'Option 2', 'Option 3', 'Add New Option']

# Use a placeholder by setting an empty string as the default value
selected_option = st.selectbox('Choose an option:', options, index=0)

# Handling placeholder behavior by checking if the first option is selected
if selected_option == options[0]:
    st.write("Please select a valid option above.")
elif selected_option == 'Add New Option':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')


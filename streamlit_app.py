import streamlit as st
import pandas as pd
import numpy as np

# List of options (without a default value at the start)
options = ['Option 1', 'Option 2', 'Option 3', 'Add New Option']

# Add a special placeholder value (empty string or None) to simulate the placeholder
options_with_placeholder = [' '] + options

# Use the selectbox, with 'Select an option' as the placeholder
selected_option = st.selectbox('Choose an option:', options_with_placeholder)

# Logic to handle when the placeholder is selected
if selected_option == 'Select an option':
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



import streamlit as st
import pandas as pd
import numpy as np

# Dropdown selection
options = ['+ Add New Option','Option 1', 'Option 2', 'Option 3']
selected_option = st.selectbox('Choose an option:', options)

# Input for new options (if "Add New" is selected)
if selected_option == '+ Add New Option':
    new_option = st.text_input('Enter a new option:')
    if st.button('Add'):
        if new_option:
            options.append(new_option)
            st.success(f"New option '{new_option}' added!")
        else:
            st.error("Please enter a new option.")


# Dropdown menu
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])

# Spacer to make the layout cleaner
st.write("") 

# Button for the action
if st.button('Add New Option'):
    st.write(f'You chose: {option}. Now you can add a new option!')

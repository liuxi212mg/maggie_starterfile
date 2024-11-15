import streamlit as st
import pandas as pd
import numpy as np

# Dropdown menu with placeholder option as the first item
Select_Prompt = ['Select an option below', '+ Add New Prompt', 'A mystical, enchanted forest at dusk, where the trees are ancient and towering, their gnarled branches twisted and covered in moss. The forest floor is blanketed with thick, lush green grass and vibrant wildflowers in shades of purple, blue, and pink. In the distance, a sparkling, winding stream reflects the last light of the setting sun', 'Option 3']
selected_option = st.selectbox('Choose an option:', options)

# Handling the placeholder behavior
if selected_option == 'Select an option':
    st.write("Please select an option above.")
elif selected_option == '+ Add New Prompt':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')


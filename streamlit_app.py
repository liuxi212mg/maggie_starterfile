import streamlit as st
import pandas as pd
import numpy as np

# Dropdown menu with an "Add New Option" choice
options = ['A mystical, enchanted forest at dusk, where the trees are ancient and towering, their gnarled branches twisted and covered in moss. The forest floor is blanketed with thick, lush green grass and vibrant wildflowers in shades of purple, blue, and pink. In the distance, a sparkling, winding stream reflects the last light of the setting sun', 'Option 2', 'Option 3', '+ Add New Option']
selected_option = st.selectbox('Choose an option:', options)

if selected_option == 'Add New Option':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')

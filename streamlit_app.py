import streamlit as st

options = ['+ Add New Option', 'Option 2', 'Option 3', 'Option 4']
options_with_placeholder = ['Select an option'] + options
selected_option = st.selectbox('Choose an option:', options_with_placeholder)

if selected_option == 'Select an option':
    st.write("Please select a valid option above.")
elif selected_option == '+ Add New Option':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')



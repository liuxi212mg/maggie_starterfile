import streamlit as st

# Define the options for the selectbox
options = ['Option 1', 'Option 2', 'Option 3', 'Add New Option']

# Use a custom selectbox with 'Add New Option' as an option
selected_option = st.selectbox('Choose an option:', options)

# CSS to style the dropdown menu, emphasizing the "Add New Option" option
st.markdown("""
<style>
    /* Add a custom style to the dropdown list container */
    .stSelectbox div[data-baseweb="select"] {
        font-size: 14px;
        color: #333;
    }
    
    /* Specifically style the "Add New Option" option */
    .stSelectbox div[data-baseweb="select"] .option:nth-child(4) {
        background-color: #ffcc00; /* Yellow background for "Add New Option" */
        color: white;  /* White text color */
        font-weight: bold; /* Make the text bold */
    }
    
    /* Option hover effect */
    .stSelectbox div[data-baseweb="select"] .option:nth-child(4):hover {
        background-color: #e6b800; /* Darken the yellow on hover */
    }
</style>
""", unsafe_allow_html=True)

# Logic for selecting options
if selected_option == 'Add New Option':
    new_item = st.text_input("Enter a new item:")
    if st.button('Add New Item'):
        if new_item:
            st.success(f"New item '{new_item}' added!")
        else:
            st.error("Please enter a new item.")
else:
    st.write(f'You selected: {selected_option}')

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)

tab1, tab2, tab3 = st.tabs(["Dax Reference Cheat Sheet - MAR2023", "Art Collection at 160 Front-6689340", "(Read Only) Mandatory pop-up window","ChatGPT Interface - Compliance Info Display Mockups"])



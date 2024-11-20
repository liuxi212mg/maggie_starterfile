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

import streamlit as st

options = ["Art Collection at 160 Front-6689340", "Investment Risk Report_Board_20241007 - FSRA_v3 ", "ChatGPT Interfaces - Compliance Info Display Mockups", "cute cute cute cat"]
selection = st.pills("Directions", options, selection_mode="single")
st.markdown(f"Your selected options: {selection}.")

import streamlit as st

options = ["Art Collection at 160 Front-6689340", "Investment Risk Report_Board_20241007 - FSRA_v3 ", "ChatGPT Interfaces - Compliance Info Display Mockups", "cute cute cute cat"]
selection = st.segmented_control(
    "Directions", options, selection_mode="single"
)
st.markdown(f"Your selected options: {selection}.")

import random
import pandas as pd
import streamlit as st

df = pd.DataFrame(
    {
        "name": ["Imagine you are a data analyst working in Ontario Teachers'' Pension Plan and want to get a quick summary of the document. You wish to know what the date difference what''s the major product difference what is the price difference who is responsible for this project and does that change over time. If yes who is the latest one. Also what is the currency for the invoice and how the service provided differ between different project. You might want to present it to the senior leadership so please keep it concise and professional. Instead of table or column for one-to-one comparison you wish to have a summary paragraph that includes all the information mentioned above. For the other irrelevant information you also want to keep that in the conversation so you didn''t miss anything important.", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
import streamlit as st

# Sample dropdown options
options = ["Option 1", "Option 2", "Option 3"]

# Select box for dropdown
selected_option = st.selectbox("Choose an option", options)

# Display some text
st.write(f"You selected: {selected_option}")



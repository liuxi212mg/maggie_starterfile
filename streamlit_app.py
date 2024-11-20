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

# Sample dropdown options
options = ["Option 1", "Option 2", "Option 3"]

# Select box for dropdown
selected_option = st.selectbox("Choose an option", options)

# Display some text
st.write(f"You selected: {selected_option}")

# Add custom CSS for hover effect
st.markdown("""
    <style>
        .hover-text {
            position: relative;
            display: inline-block;
        }

        .hover-text .tooltip {
            visibility: hidden;
            width: 150px;
            background-color: black;
            color: #fff;
            text-align: center;
            border-radius: 5px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 100%;
            left: 50%;
            margin-left: -75px;
        }

        .hover-text:hover .tooltip {
            visibility: visible;
        }
    </style>
""", unsafe_allow_html=True)



# Tooltip display for options
st.markdown(f'''
    <div class="hover-text">
        Hover over this text to see the tooltip!
        <span class="tooltip">This is a tooltip!</span>
    </div>
''', unsafe_allow_html=True)





# Define the options for the selectbox with longer descriptions
options = [
    ("Option 1", "This is a detailed description of Option 1. It includes extra information about this choice."),
    ("Option 2", "Here is Option 2. This one has some important details too, explaining why it's a great choice."),
    ("Option 3", "Option 3 has its own unique benefits. Here is a brief summary of what this option offers."),
    ("Add New Option", "You can add a new option to the list by selecting this choice.")
]

# Extract the labels and descriptions separately
labels = [item[0] for item in options]
descriptions = {item[0]: item[1] for item in options}

# Display the selectbox with the user-friendly labels
selected_option = st.selectbox('Choose an option:', labels)

# CSS for showing the full description on hover
st.markdown("""
<style>
    /* Style the dropdown options */
    .stSelectbox div[data-baseweb="select"] {
        font-size: 14px;
        color: #333;
    }
    
    /* Style the option text with ellipsis for overflow */
    .stSelectbox div[data-baseweb="select"] .option {
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
    }

    /* Tooltip style for the full content */
    .tooltip {
        visibility: hidden;
        width: 300px;
        background-color: #333;
        color: white;
        text-align: center;
        border-radius: 5px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 100%;
        left: 50%;
        margin-left: -150px;
        opacity: 0;
        transition: opacity 0.3s;
    }

    /* Show the tooltip on hover */
    .hover-text:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }
</style>
""", unsafe_allow_html=True)

# Display the options with tooltips, ensuring each has a unique ID
for i, label in enumerate(labels):
    st.markdown(f'''
        <div class="hover-text" id="hover-text-{i}">
            <div>{label}</div>
            <span class="tooltip">{descriptions[label]}</span>
        </div>
    ''', unsafe_allow_html=True)











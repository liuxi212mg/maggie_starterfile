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
    ("Option 3", "Option 3 has its own unique benefits. Here is a brief summary of what this option offers.")
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


import streamlit as st

# Custom HTML and CSS for the Dropdown Menu and Tooltips
dropdown_html = """
    <style>
        /* Styling the dropdown button */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown-button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }

        /* Dropdown menu style */
        .dropdown-menu {
            display: none;
            position: absolute;
            background-color: #f1f1f1;
            min-width: 160px;
            box-shadow: 0px 8px 16px rgba(0,0,0,0.2);
            z-index: 1;
        }

        .dropdown:hover .dropdown-menu {
            display: block;
        }

        /* Style for each item in the dropdown */
        .dropdown-item {
            padding: 12px 16px;
            display: block;
            color: black;
            text-decoration: none;
            font-size: 14px;
        }

        .dropdown-item:hover {
            background-color: #ddd;
        }

        /* Tooltip styling */
        .tooltip {
            visibility: hidden;
            width: 200px;
            background-color: #555;
            color: #fff;
            text-align: center;
            border-radius: 5px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 100%; /* Position the tooltip above */
            left: 50%;
            margin-left: -100px;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .dropdown-item:hover .tooltip {
            visibility: visible;
            opacity: 1;
        }
    </style>

    <div class="dropdown">
        <button class="dropdown-button">Select an option</button>
        <div class="dropdown-menu">
            <a href="#" class="dropdown-item">
                Option 1
                <span class="tooltip">Explanation for Option 1</span>
            </a>
            <a href="#" class="dropdown-item">
                Option 2
                <span class="tooltip">Explanation for Option 2</span>
            </a>
            <a href="#" class="dropdown-item">
                Option 3
                <span class="tooltip">Explanation for Option 3</span>
            </a>
            <a href="#" class="dropdown-item">
                Option 4
                <span class="tooltip">Explanation for Option 4</span>
            </a>
        </div>
    </div>
"""

# Display the HTML in Streamlit
st.markdown(dropdown_html, unsafe_allow_html=True)

# You can also add other Streamlit widgets below, such as:
# st.write("Some other content")

genre = st.sidebar.radio(
    "Model Choice",
    ["GPT-4o", "GPT-4o mini", "GPT-4","GPT-4 32K", "GPT-3.5 Turbo","GPT-3.5 Turbo 16K","o1-preview","o1-mini"],
    captions=[
        "High-performance for complex tasks",
        "Faster, lightweight GPT-4o version",
        "Deep understanding and creativity",
        "Handles large context and documents",
        "Fast for simple tasks",
        "Extended context handling variant",
        "Advanced, broad world knowledge model",
        "Faster, cost-effective reasoning model"
    ],
)


import streamlit as st

# Create an expander to contain the radio button widget
with st.expander("Choose Model Type"):
    genre = st.sidebar.radio(
        "Model Choice",
        ["GPT-4o", "GPT-4o mini", "GPT-4", "GPT-4 32K", "GPT-3.5 Turbo", "GPT-3.5 Turbo 16K", "o1-preview", "o1-mini"],
        captions=[
            "High-performance for complex tasks",
            "Faster, lightweight GPT-4o version",
            "Deep understanding and creativity",
            "Handles large context and documents",
            "Fast for simple tasks",
            "Extended context handling variant",
            "Advanced, broad world knowledge model",
            "Faster, cost-effective reasoning model"
        ],
    )




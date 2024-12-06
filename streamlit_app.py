
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



import streamlit as st

# Expanded help text with bold model names and more descriptions
help_txt = '''- **GPT-4o (Recommended)**: High accuracy for complex, multi-step tasks.
GPT-4o mini: variant of 4o, faster response with lower resources used.
- **GPT-4**: Excels in creative and technical writing tasks.
GPT-4 32K: Handles large context and documents.
- **GPT-3.5 Turbo**: Fast for simpler tasks with good performance.
GPT-3.5 Turbo 16K: Extended context handling variant.
- **o1-preview**: Advanced reasoning model with broad world knowledge.
o1-mini: Faster reasoning model for simpler tasks.'''

# List of models for the selectbox
models = [
    "GPT-4o", "GPT-4o mini", "GPT-4", "GPT-4 32K", "GPT-3.5 Turbo", 
    "GPT-3.5 Turbo 16K", "o1-preview", "o1-mini"
]

# Place everything inside the sidebar
with st.sidebar:
    # No need to convert to bytes, just use the string
    # Displaying the bytes converted help text (although this won't render markdown correctly)
    bytes_help_txt = bytes(help_txt, 'utf-8')

    # Adjust the help text by replacing line breaks with a formatted version
    new_line = '\n'
    mod_help_txt = help_txt.replace(new_line, '  ' + new_line)  # Adds extra spaces before line breaks

    # Create a selectbox with the expanded help content
    selected_model = st.selectbox("Select a Model", models, help=mod_help_txt)



import streamlit as st

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

options = ["Major Product Difference", "Generate Summary"]
selection = st.pills("Directions", options, selection_mode="multi")

import streamlit as st

options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

st.write("You selected:", options)


import streamlit as st
import pandas as pd

# Title or Header
st.title("Results")

# Subheader for Prompt Title Section
st.subheader("Prompt Title(s):")

# Radio buttons for selecting a prompt
prompt_choice = st.radio("", ["Major Product Difference", "Generate Summary"], horizontal=True)

# Results Table Section
st.write("### Results")

# Example data for the table
data = {
    "File": ["AI Builder Prompting Guide"],
    "Answer": ["placeholderplaceholder"]
}

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Display table
st.table(df)

# Download button
st.download_button(
    label="Download Generated Results",
    data="Generated Results Content Here",  # Replace with your generated content
    file_name="results.txt",
    mime="text/plain"
)

# Add space for further user actions or processing
st.markdown("**Additional actions can be added below as needed.**")










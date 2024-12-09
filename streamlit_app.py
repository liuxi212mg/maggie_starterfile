

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
import pandas as pd

# Inject custom CSS for styles
st.markdown(
    """
    <style>
    /* Title styling */
    .title-style {
        font-family: 'Montserrat', sans-serif;
        font-size: 24px;
        font-weight: bold;
        color: #262730;
        display: inline-block; /* Allow inline placement */
    }

    /* Download button styling */
    .download-button {
        background-color: #606060 !important;
        color: white !important;
        border: none !important;
        padding: 8px 16px !important;
        border-radius: 5px !important;
        font-family: 'Sources Sans Pros', sans-serif;
        font-size: 14px !important;
        display: inline-block; /* Align inline with title */
        margin-left: 20px; /* Space between title and button */
        cursor: pointer;
    }

    /* Align "Prompt Titles" and radio buttons */
    .prompt-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px; /* Space below the container */
    }

    /* Prompt Titles styling */
    .prompt-titles {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 16px;
        font-weight: normal;
        color: #262730;
        margin-right: 10px; /* Space between text and radio buttons */
    }

    /* DataFrame header styling */
    .dataframe-header {
        font-family: 'Montserrat', sans-serif;
        font-size: 16px;
        font-weight: bold;
        color: #8A8A8A;
        text-align: left;
    }

    /* Table cell styling */
    .dataframe-cell {
        font-family: 'Montserrat', sans-serif;
        font-size: 14px;
        color: #606060;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Results title with Download button on the same line
st.markdown(
    """
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div class="title-style">Results</div>
        <button class="download-button">Download Generated Results</button>
    </div>
    """,
    unsafe_allow_html=True,
)


# Radio buttons for selecting a prompt, aligned horizontally
options = ["Major Product Difference", "Generate Summary"]
selection = st.pills("Directions", options, selection_mode="single",label_visibility="hidden")

from openai import OpenAI
import streamlit as st

st.title("ChatGPT-like clone")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})















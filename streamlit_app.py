

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
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Title and introductory text
st.title("OTPP Secured Chatbot")
st.text("Address users’ questions through conversational interaction, ensuring secure management of confidential data.")

# Display pills (tags) above the input field
pill_labels = [
    "Can you help me debug my code?", 
    "I want to summarize a document.", 
    "I want some inspiration", 
    "FAQ", 
    "Contact Us"
]

# Create pills and handle their interactions
selected_pills = st.pills(
    label="Choose an option:",
    options=pill_labels,
    selection_mode="single",  # Can select only one pill at a time
)

# Respond based on the selected pill
if selected_pills:
    if selected_pills == pill_labels[0]:
        st.session_state.messages.append({"role": "assistant", "content": "What code do you need help with?"})
    elif selected_pills == pill_labels[1]:
        st.session_state.messages.append({"role": "assistant", "content": "Of course. Please enter the text you want me to summarize."})
    elif selected_pills == pill_labels[2]:
        st.session_state.messages.append({"role": "assistant", "content": "What areas do you need inspiration in?"})
    elif selected_pills == pill_labels[3]:
        st.session_state.messages.append({"role": "assistant", "content": "Feel free to ask any questions from the FAQ!"})
    elif selected_pills == pill_labels[4]:
        st.session_state.messages.append({"role": "assistant", "content": "Please contact us through our support page for assistance."})

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
















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

# Title and description
st.title("OTPP Secured Chatbot")
st.text("Address users’ questions through conversational interaction, ensuring secure management of confidential data.")

# Initialize chat history
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


import streamlit as st

# Title and description
st.title("OTPP Secured Chatbot")
st.text("Address users’ questions through conversational interaction, ensuring secure management of confidential data.")

# Initialize chat history if not already in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate chatbot responses (this is a placeholder for now)
def response_generator(user_input):
    return f"Assistant says: '{user_input}'"

# Create a form with a submit button
with st.form(key="chat_form"):
    instr = 'Hi there! Enter what you want to let me know here.'
    
    # Handle dynamic enabling/disabling of input based on prompt selection
    user_input = st.text_input(
        instr,
        placeholder=instr,  # Instruction for the user to enter something
        label_visibility='collapsed',  # Hide label
    )
    
    # Define prompt suggestions dropdown (this will be below the text input)
    init_prompt = st.selectbox(
        'You might want to try these prompts...',
        ['<Click Me to Expand>',
         'How to socialize?',
         'How to focus on tasks?',
         'How to find peace in daily work?']
    )
    
    # If the initial prompt is selected, fill the text input with that prompt
    if init_prompt != '<Click Me to Expand>':
        user_input = init_prompt

    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Trigger actions only when the form is submitted
if submit_button and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate assistant response
    response = response_generator(user_input)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)












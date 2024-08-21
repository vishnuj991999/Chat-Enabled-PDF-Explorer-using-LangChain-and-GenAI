import streamlit as st
from utils import load_and_process_pdf, setup_together_client
from chat import handle_user_input

# Streamlit UI
st.subheader("Chat with PDF")

# Initialize session state for storing chat history and memory
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# PDF file uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# If a file is uploaded, process it
if uploaded_file is not None:
    system_content = load_and_process_pdf(uploaded_file)

    # Display chat history
    for i, chat in enumerate(st.session_state['chat_history']):
        st.write(f"User: {chat['role']} | Content: {chat['content']}")  # Display each message
        st.markdown("---")

    # User input for question
    user_prompt = st.chat_input("Ask anything about the content...")

    if user_prompt:
        handle_user_input(user_prompt, system_content)
else:
    st.write("Please upload a PDF file to continue.")

import streamlit as st
from streamlit_chat import message
from utils import setup_together_client

def handle_user_input(user_prompt, system_content):
    """Process user input and generate a response."""
    together_client = setup_together_client()

    # Add the user's question to chat history and display it
    st.session_state['chat_history'].append({"role": "user", "content": user_prompt})
    message(user_prompt, is_user=True, key=f"user_message_{len(st.session_state['chat_history'])}")

    # Send the question to the model
    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_prompt}
        ],
        max_tokens=1000,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"],
    )

    # Get the response from the model
    assistant_response = response.choices[0].message.content

    # Add the assistant's response to chat history and display it
    st.session_state['chat_history'].append({"role": "assistant", "content": assistant_response})
    message(assistant_response, key=f"assistant_message_{len(st.session_state['chat_history'])}")

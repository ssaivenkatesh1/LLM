import streamlit as st
import requests

class ChatUI:
    """
    Handles the Streamlit-based chat user interface.
    """

    def __init__(self):
        """
        Set up the Streamlit UI page config and initialize session state.
        """
        st.set_page_config(page_title="Local LLM Chat", layout="centered")
        st.title("💬 Local LLM Chat")

        if "history" not in st.session_state:
            st.session_state["history"] = []

    def display_chat(self):
        """
        Display the chat history from session state in the Streamlit UI.
        """
        for sender, msg in st.session_state["history"]:
            with st.chat_message("user" if sender == "user" else "assistant"):
                st.markdown(msg)

    def send_and_receive(self, user_input):
        """
        Send the user's message to the backend and append the response to the chat history.

        :param user_input: The message typed by the user.
        """
        st.session_state["history"].append(("user", user_input))

        with st.spinner("Thinking..."):
            response = requests.post(
                "http://backend:8000/chat",
                json={"message": user_input}
            )
            bot_msg = response.json()["response"]
            st.session_state["history"].append(("bot", bot_msg))

    def run(self):
        """
        Main loop: captures user input, triggers response generation, and displays chat.
        """
        user_input = st.chat_input("Ask something...")
        if user_input:
            self.send_and_receive(user_input)

        self.display_chat()

# Run the Streamlit app
if __name__ == "__main__":
    app = ChatUI()
    app.run()

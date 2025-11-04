import streamlit as st
import os
import logging
import requests
import asyncio
import sys

# Fix for Streamlit event loop on Windows
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

st.title("Chatbot")

# Get backend URL from environment variable, with a fallback for local development
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8001")

# Document Upload UI
st.header("Upload Documents")
uploaded_file = st.file_uploader("Choose a document", type=["pdf", "txt", "docx", "md"])

if uploaded_file is not None:
    file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type}
    logger.info(f"Attempting to upload file: {file_details}")
    st.write(file_details)

    st.session_state.processing_status = "Uploading..."
    st.write(f"Status: {st.session_state.processing_status}")

    try:
        files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        response = requests.post(f"{BACKEND_URL}/upload", files=files)

        if response.status_code == 200:
            st.session_state.processing_status = "Processing..."
            st.write(f"Status: {st.session_state.processing_status}")
            # The backend now handles the processing. We can show the response from the backend.
            st.success(f"Document '{uploaded_file.name}' uploaded successfully! Backend response: {response.json()}")
            logger.info(f"Document '{uploaded_file.name}' uploaded successfully.")
            st.session_state.processing_status = "Ready"
        else:
            st.session_state.processing_status = "Error"
            st.error(f"Error uploading document: {response.text}")
            logger.error(f"Error uploading document '{uploaded_file.name}': {response.text}")

    except Exception as e:
        st.session_state.processing_status = "Error"
        st.error(f"Error uploading file: {e}")
        logger.error(f"Error uploading file '{uploaded_file.name}': {e}", exc_info=True)


# Chat Interface
st.header("Ask a Question")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What do you want to know?"):
    logger.info(f"User asked: {prompt}")
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            payload = {"question": prompt}
            response = requests.post(f"{BACKEND_URL}/ask", json=payload)
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.markdown(answer)
                logger.info(f"Assistant replied: {answer}")
            else:
                answer = "An error occurred while trying to answer your question. Please try again later."
                st.error(answer)
                logger.error(f"Error answering question '{prompt}': {response.text}")
        except Exception as e:
            answer = "An error occurred while trying to answer your question. Please try again later."
            st.error(answer)
            logger.error(f"Error answering question '{prompt}': {e}", exc_info=True)
    st.session_state.messages.append({"role": "assistant", "content": answer})
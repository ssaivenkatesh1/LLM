import ollama

def extract_tasks(text):
    """
    Extracts tasks from a text using the Ollama library.
    """
    client = ollama.Client(host='http://host.docker.internal:11434')
    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': f"Please extract all action items and tasks from the following meeting transcript. Present them as a numbered list.:\n\n{text}",
        },
    ])
    return response['message']['content']

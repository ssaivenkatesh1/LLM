import ollama

def summarize_text(text):
    """
    Summarizes a text using the Ollama library to generate structured notes.
    """
    print("Text = ",text)
    client = ollama.Client(host='http://host.docker.internal:11434')
    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': f"Please summarize the following meeting transcript and extract key decisions and action items:\n\n{text}",
        },
    ])
    print("Response = ",response['message']['content'])
    return response['message']['content']

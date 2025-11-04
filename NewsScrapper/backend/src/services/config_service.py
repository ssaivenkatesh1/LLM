# In a real application, this would read from and write to a persistent store like a database or a config file.
# For simplicity, we'll use an in-memory dictionary.
config = {"llm_provider": "gemini"}

def get_config():
    return config

def update_config(new_config: dict):
    global config
    config.update(new_config)
    return config

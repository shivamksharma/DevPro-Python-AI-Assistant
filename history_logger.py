from datetime import datetime

def log_conversation(user_input, assistant_response):
    """
    Log user input and assistant response to a file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("conversation_history.txt", "a") as file:
        file.write(f"[{timestamp}] User: {user_input}\n")
        file.write(f"[{timestamp}] Assistant: {assistant_response}\n")  
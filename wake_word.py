import speech_recognition as sr

def listen_for_wake_word(wake_word, record_audio_function):
    """
    Listen for the wake word to activate the assistant.
    """
    print(f"Listening for wake word '{wake_word}'...")
    while True:
        voice_data = record_audio_function()
        if wake_word.lower() in voice_data.lower():
            return True
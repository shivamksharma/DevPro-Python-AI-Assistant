#!/usr/bin/python3

import speech_recognition as sr
from gtts import gTTS
import random
from time import ctime
import time
import webbrowser
import yfinance as yf
import playsound
import os

class User:
    def __init__(self):
        self.name = ''

    def set_name(self, name):
        self.name = name

user_obj = User()

def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not understand. Kindly rephrase your question.')
        except sr.RequestError:
            speak('Sorry, I am unable to process your request at the moment.')
        print(f">> {voice_data.lower()}")
        return voice_data.lower()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = f'audio{r}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(f"devpro: {audio_string}")
    os.remove(audio_file)

def respond(voice_data):
    if any(greeting in voice_data for greeting in ['hey', 'hi', 'hello', 'bonjour', 'hola']):
        greetings = [f"Hey, how can I help you, {user_obj.name}?",
                     f"Hey, what's up, {user_obj.name}?",
                     f"I'm listening, {user_obj.name}. How can I assist you?",
                     f"How can I help you, {user_obj.name}?",
                     f"Hello, {user_obj.name}!"]
        greet = random.choice(greetings)
        speak(greet)

    if any(name_question in voice_data for name_question in ["what is your name", "what's your name", "tell me your name"]):
        if user_obj.name:
            speak("My name is Devprogramming.")
        else:
            speak("My name is Devprogramming. What's your name?")

    if "my name is" in voice_data:
        person_name = voice_data.split("is")[-1].strip()
        speak(f"Okay, I will remember that, {person_name}.")
        user_obj.set_name(person_name)

    if any(how_question in voice_data for how_question in ["how are you", "how are you doing"]):
        speak(f"I'm very well, thanks for asking, {user_obj.name}.")

    if any(time_question in voice_data for time_question in ["what's the time", "tell me the time", "what time is it"]):
        current_time = ctime().split(" ")[3].split(":")[0:2]
        hours = '12' if current_time[0] == "00" else current_time[0]
        minutes = current_time[1]
        time_string = f'{hours} {minutes}'
        speak(time_string)

    if "search for" in voice_data and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1].strip()
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on Google.')

    if "youtube" in voice_data:
        search_term = voice_data.split("for")[-1].strip()
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on YouTube.')

    if "price of" in voice_data:
        search_term = voice_data.lower().split(" of ")[-1].strip()
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]
            currency = stock.info["currency"]
            speak(f'The price of {search_term} is {price} {currency}, {user_obj.name}.')
        except:
            speak('Oops, something went wrong.')

    if any(exit_command in voice_data for exit_command in ["exit", "quit", "goodbye"]):
        speak("Going offline.")
        exit()

if __name__ == "__main__":
    time.sleep(1)
    while True:
        voice_data = record_audio()
        respond(voice_data)

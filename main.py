import speech_recognition as speech_recognition
import plysound
from gtts import gtts
import random
from time import ctime
import webbrowser
import ssl
import certifi
import time
import os

class person:
    name = ''
    def setName(self, name):
        self.name = name
        
def there_exists(terms):
  for term in terms:
    if term in voice_data:
        return True
    
r = sr.Recognizer() 
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry I did not understand, Kindly Rephrase your question')
        except sr.RequestError:
            speak('Sorry, Iam Down')
        print(f">> {voice_data.lower()}")
        return voice_data.lower()
    
    
def speak(audio_string):
    tts = gtts(text=audio_string, lang='en')
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file) 
    print(f"kiri: {audio_string}")
    os.remove(audio_file)
    
    
def  respond(voice_data):
    if there_exists(['hey','hi','hello','bonjour','hola']):
        greetings = [f"hey, how can I help you to test this assistant application {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet) 
        
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person_obj.name:
            speak("my name is Devprogramming")
        else:
            speak("my name is Devprogramming. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)
        
        
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person_obj.name}")

        
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)
        
        
        

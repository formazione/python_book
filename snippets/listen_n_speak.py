#%%
#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
# from gtts import gTTS
from win32com.client import Dispatch
import sys


print(sys.version)
def speak(audioString):
    print(audioString)
    s = Dispatch("SAPI.SpVoice")
    s.Speak(audioString)


# def speak(audioString):
#     print(audioString)
#     tts = gTTS(text=audioString, lang='en')
#     tts.save("audio.mp3")
#     os.system("mpg321 audio.mp3")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSay something!... (stop to close this app)")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="")`

        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("Sto bene")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Nukes, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# initialization
# time.sleep(4)
# speak("Hi Nukes, what can I do for you?")
while 1:
    data = recordAudio()
    if data == "stop":
        break
    jarvis(data)
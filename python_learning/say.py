import cowsay # used for draw ascii drawings
import pyttsx3 # used for text to speech converter

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i in range(2):
    engine.setProperty('voice', voices[i].id)
    this = input("What's this? ")
    cowsay.cow(this)
    engine.say(this)
    engine.runAndWait()
engine.stop()
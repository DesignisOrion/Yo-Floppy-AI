import pyttsx3 as p
import speech_recognition as sr
import datetime

engine = p.init()

# speed fof the voice
rate = engine.getProperty('rate')
engine.setProperty('rate',180)  #rate of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # using female voice [1]. Male voice [0]
print(voices)
engine.say("I am your YO FLOPPY assistant. How can I help you today!")
engine.runAndWait() # time waiting for the voice to finish


r = sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening...")
    text=r.recognize_google(audio)
    audio = r.listen(source)
    print(text)
    
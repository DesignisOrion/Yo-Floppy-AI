import pyttsx3 as p

engine = p.init()

# speed fof the voice
rate = engine.getProperty('rate')
engine.setProperty('rate',180)  #rate of voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # using female voice [1]. Male voice [0]
print(voices)
engine.say("I am your YO FLOPPY assistant. How can I help you today!")
engine.runAndWait() # time waiting for the voice to finish
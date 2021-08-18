import pyttsx3 as p

engine = p.init()

# speed fof the voice
rate = engine.getProperty('rate')
engine.setProperty('rate',160)  #rate of voice
voices = engine.getProperty('voices')
print(voices)
engine.say("WELCOME TO GOLDEN FLOPPY LABS! How can I help you today Mr. Orion?.")
engine.runAndWait() # time waiting for the voice to finish
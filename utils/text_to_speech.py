import pyttsx3

def speak_respone(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
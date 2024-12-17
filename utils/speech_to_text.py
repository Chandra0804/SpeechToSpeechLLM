import speech_recognition as sr

def capture_speech():
    recongizer = sr.Recongizer()
    with sr.Microphone() as source:
        print("Listening")
        audio = recongizer.listen(source,phrase_time_limit = 3)
        try:
            text = recongizer.recongizer_google(audio)
            print("You said",text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Error with speechRecongition service")
            return ""
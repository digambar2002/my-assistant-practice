import time
import speech_recognition as sr
import pyttsx3


def speak(audio):
    
    voiceEngine = pyttsx3.init('sapi5')
    voices = voiceEngine.getProperty('voices')
    # print(voices[1].id)
    # print(voices)
    voiceEngine.setProperty('voice', voices[1].id)
    voiceEngine.setProperty('rate', 174)
    voiceEngine.say(audio)
    voiceEngine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print("Recoginizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
        # time.sleep(2)
        # eel.sleep(1.0)
    except Exception as e:
        return ""
    return query.lower()

text = takecommand()
speak(text)



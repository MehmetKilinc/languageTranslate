import speech_recognition as sr
from translate import Translator
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print("i am listening")
    audio = r.listen(source)
    metin = str(r.recognize_google(audio,language = "en"))

translator = Translator(to_lang="tr")
translation = translator.translate(metin)

print("ingilizce: " + metin)
print("türkçe: " + translation)


objec = pyttsx3.init()
objec.setProperty('rate',100)
objec.say(translation)
objec.runAndWait()

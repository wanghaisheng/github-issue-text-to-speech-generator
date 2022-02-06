import pyttsx3
from random import randint
import shutil

engine = pyttsx3.init()
voices = ["karen", "samantha", "alex", "daniel"]

def makeVoiceAt(path, text):
    engine.setProperty("rate", 210)
    voice = voices[randint(0, len(voices) - 1)]
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.{}".format(voice))
    engine.say(text)
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()
    engine.stop()
    shutil.move("speech.mp3", path+"/speech.mp3")

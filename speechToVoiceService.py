import pyttsx3
from random import randint
import shutil

class SpeechToVoiceService:
    voices = ["karen", "samantha", "alex", "daniel"]
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()

    def makeVoiceAt(self, path, text):
        print("called the speechservice")
        self.engine.setProperty("rate", 210)
        print("1")
        voice = self.voices[randint(0, len(self.voices) - 1)]
        self.engine.setProperty("voice", "com.apple.speech.synthesis.voice.{}".format(voice))
        self.engine.say(text)
        print("2")
        self.engine.save_to_file(text, path + ".mp3")
        print("3")
        self.engine.runAndWait()
        print("4")
        # self.engine.stop()
        print("saved audio at path {}".format(path))
        # shutil.move("speech.mp3", path+"/speech.mp3")

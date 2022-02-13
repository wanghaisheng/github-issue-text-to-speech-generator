import pyttsx3
from random import randint
import shutil
from gtts import gTTS

class SpeechToVoiceService:
    voices = ["karen", "samantha", "alex", "daniel"]
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 210)

    def makeVoiceAt(self, path, text):
        # print("called the speechservice")
        # print("1")
        # self.engine = pyttsx3.init()
        # self.engine.setProperty("rate", 210)
        # voice = self.voices[randint(0, len(self.voices) - 1)]
        # self.engine.setProperty("voice", "com.apple.speech.synthesis.voice.{}".format(voice))
        # print("2")
        # # self.engine.save_to_file(text, path + ".mp3")
        # self.engine.say(text)
        # print("3")
        # self.engine.runAndWait()
        # print("4")
        # self.engine.stop()
        # print("saved audio at path {}".format(path))
        # # shutil.move("speech.mp3", path+"/speech.mp3")
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save(path + ".mp3")

import pyttsx3
from random import randint


class SpeechToVoiceService:
    voices = ["karen", "samantha", "alex", "daniel"]
    engine = None

    def makeVoiceAt(self, path, text):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 180)
        voice = self.voices[randint(0, len(self.voices) - 1)]
        self.engine.setProperty("voice", "com.apple.speech.synthesis.voice.{}".format(voice))
        self.engine.save_to_file(text, path + ".mp3")
        self.engine.runAndWait()
        del self.engine
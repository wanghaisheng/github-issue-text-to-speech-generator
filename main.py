from Reddit import RedditService
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import pyttsx3
import shutil
from random import randint

driver = ""  ## the chrome web driver
engine = pyttsx3.init()
voices = ["karen", "samantha", "alex", "daniel"]


def setDriver():
    global driver

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    url = "file:///Users/tigran/Desktop/redditPage.html"
    driver.get(url)
    return driver


def screenshot():
    global driver

    element = driver.find_element(By.CLASS_NAME, "_1oQyIsiPHYt6nx7VOmd1sz")

    element.screenshot("ss.png")
    screenshot = Image.open("ss.png")
    screenshot.show()


def startScrapping():
    global driver

    driver = setDriver()
    screenshot()


def mkdirIfExists(path):
    if os.path.isdir(path):
        print("path {} exists".format(path))
        return
    else:
        os.mkdir(path)  # new directory


def makeVideoFrom(submission):
    folderPath = "./videos/new/askReddit_{}".format(submission.id)
    if os.path.isdir(folderPath):
        print("path {} exists, something is wrong".format(folderPath))
        return
    else:
        os.mkdir(folderPath)  # new directory
        print("creating new directory {}".format(folderPath))

    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments")


def makePostVideoAt(path, submission):
    mkdirIfExists(path)
    #takePostScreenshotAt(path, submission)
    makeVoiceAt(path, submission.title)
    # clipTogether(screenshot, voice)
    pass


def makeVoiceAt(path, text):
    engine.setProperty("rate", 210)
    voice = voices[randint(0, len(voices) - 1)]
    engine.setProperty("voice", "com.apple.speech.synthesis.voice.{}".format(voice))
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()
    engine.stop()
    shutil.move("speech.mp3", path+"/speech.mp3")


def makeCommentsVideosAt(path, submission):
    pass


if __name__ == '__main__':
    # RedditService.startSession()
    # submissions = RedditService.getHotSubmissions()
    # for submission in submissions:
    #     if submission.num_comments > 2000 and submission.score > 5000:
    #         print("saving submisiion")
    #         makeVideoFrom(submission)
    makeVoiceAt("./videos/new/askReddit_{}".format("skzwrs"), "What is a socially unacceptable thing that you dont like or hate")

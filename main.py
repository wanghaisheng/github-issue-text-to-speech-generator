import random

from Reddit import RedditService
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

driver = ""  ## the chrome web driver


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


# startScrapping()
RedditService.startSession()
RedditService.getPosts()

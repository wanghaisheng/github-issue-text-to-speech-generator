from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
_driverIsSetted = False

def _setDriver():
    global driver

    url = "file:///Users/tigran/Desktop/redditPage.html"
    driver.get(url)
    return driver


def screenshotPostAt(path, submission):
    if not _driverIsSetted:
        _setDriver()

    global driver

    postElement = driver.find_element(By.CLASS_NAME, "_1oQyIsiPHYt6nx7VOmd1sz")
    titleElement = postElement.find_element(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
    driver.execute_script("arguments[0].innerText = 'asdasdasd'", titleElement)

    postElement.screenshot(path+"/screenshot.png")
    screenshot = Image.open(path+"/screenshot.png")
    screenshot.show()

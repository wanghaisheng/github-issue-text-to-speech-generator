from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

_driverIsSetted = False

def _setDriver():
    options = Options()
    options.add_argument("window-size=850,1000")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    url = "file:///Users/tigran/Desktop/redditPage.html"
    driver.get(url)

    return  driver
def screenshotPostAt(path, submission):
    driver = _setDriver()

    postElement = driver.find_element(By.CLASS_NAME, "_1oQyIsiPHYt6nx7VOmd1sz")
    titleElement = postElement.find_element(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
    upwoteDiv = postElement.find_element(By.CLASS_NAME, "_1rZYMD_4xY3gRcSS3p8ODO")
    authorElement = postElement.find_element(By.CLASS_NAME, "_2tbHP6ZydRpjI44J3syuqC")

    print(submission.author)
    print(submission.score)
    print(submission.title)
    driver.execute_script('arguments[0].innerText = "u/{}"'.format(str(submission.author).replace('"', "'")), authorElement)
    driver.execute_script('arguments[0].innerText = "{}"'.format(str(submission.score).replace('"', "'")), upwoteDiv)
    driver.execute_script('arguments[0].innerText = "{}"'.format(str(submission.title).replace('"', "'")), titleElement)

    postElement.screenshot(path+"/screenshot.png")
    screenshot = Image.open(path+"/screenshot.png")
    screenshot.show()

def screenshotCommentAt(path, comment):
    driver = _setDriver()

    commentElement = driver.find_element(By.CLASS_NAME, "P8SGAKMtRxNwlmLz1zdJu")
    authorElement  = commentElement.find_element(By.CLASS_NAME, "wM6scouPXXsFDSZmZPHRo")
    upwoteElement = commentElement.find_element(By.CLASS_NAME, "_1rZYMD_4xY3gRcSS3p8ODO")
    paragraphElement = commentElement.find_element(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")

    driver.execute_script('arguments[0].innerText = "u/{}"'.format(str(comment.author.name).replace('"', "'")), authorElement)
    driver.execute_script('arguments[0].innerText = "{}"'.format(str(comment.score).replace('"', "'")), upwoteElement)
    driver.execute_script('arguments[0].innerText = "{}"'.format(str(comment.body).replace('"', "'")), paragraphElement)

    commentElement.screenshot(path+"/comment.png")
    screenshot = Image.open(path+"/comment.png")
    screenshot.show()
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class ScreenshotService:
    driver = None

    def __init__(self):
        self.initDriver()

    def initDriver(self):
        options = Options()
        options.add_argument("window-size=700,1000")
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        url = "file:///Users/tigran/Desktop/redditPage.html"
        self.driver.get(url)

    def screenshotPostAt(self, path, submission):
        self.initDriver()
        postElement = self.driver.find_element(By.CLASS_NAME, "_1oQyIsiPHYt6nx7VOmd1sz")
        titleElement = postElement.find_element(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
        upwoteDiv = postElement.find_element(By.CLASS_NAME, "_1rZYMD_4xY3gRcSS3p8ODO")
        authorElement = postElement.find_element(By.CLASS_NAME, "_2tbHP6ZydRpjI44J3syuqC")

        self.driver.execute_script('arguments[0].innerText = "u/{}"'.format(str(submission.author).replace('"', "'")),
                                   authorElement)
        self.driver.execute_script('arguments[0].innerText = "{}"'.format(str(submission.score).replace('"', "'")),
                                   upwoteDiv)
        self.driver.execute_script('arguments[0].innerText = "{}"'.format(str(submission.title).replace('"', "'")),
                                   titleElement)

        postElement.screenshot(path + ".jpg")

    def screenshotCommentAt(self, path, comment):
        self.initDriver()
        commentElement = self.driver.find_element(By.CLASS_NAME, "P8SGAKMtRxNwlmLz1zdJu")
        authorElement = commentElement.find_element(By.CLASS_NAME, "wM6scouPXXsFDSZmZPHRo")
        upwoteElement = commentElement.find_element(By.CLASS_NAME, "_1rZYMD_4xY3gRcSS3p8ODO")
        paragraphElement = commentElement.find_element(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")

        try:
            self.driver.execute_script(
                'arguments[0].innerText = "u/{}"'.format(str(comment.author.name).replace('"', "'")),
                authorElement)
            self.driver.execute_script('arguments[0].innerText = "{}"'.format(str(comment.score).replace('"', "'")),
                                       upwoteElement)
            self.driver.execute_script('arguments[0].innerText = "{}"'.format(str(comment.body).replace('"', "'")),
                                       paragraphElement)

            commentElement.screenshot(path + ".jpg")
        except:
            print("couldn't save the screenshot, error at {}".format(path))

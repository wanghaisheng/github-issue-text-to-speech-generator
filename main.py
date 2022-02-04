from Reddit import RedditService
from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def setDarkMode(driver):
    driver.find_element_by_class_name("_10K5i7NW6qcm-UoCtpB3aK").click() ## open user page
    driver.find_element_by_class_name("_2KotRmn9DgdA58Ikji2mnV").click() ## tap on dark mode

def setDriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("start-maximized")
    # chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    url = "https://www.reddit.com/r/AskReddit/comments/siq2ts/redditors_who_used_the_internet_back_when_it_was/"
    driver.get(url)
    return driver

def closeAlertIfNeeded(driver):
    try:
        WebDriverWait(driver, 8).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        print("no alert")

def screenshot(driver):
    print("sleeping")
    time.sleep(15)
    print("sleeping finished")
    closeAlertIfNeeded(driver)
    element = driver.find_element_by_id("t3_siq2ts")
    element.screenshot("ss.png")
    screenshot = Image.open("ss.png")
    screenshot.show()

driver = setDriver()
setDarkMode(driver)
screenshot(driver)


# RedditService.startSession()
# RedditService.getPosts()

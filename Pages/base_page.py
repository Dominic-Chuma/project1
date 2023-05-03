# mypackage.average(3,3)
from selenium import webdriver

# To use time
# import time as sl
# To use Chrome webdriver manager.
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
# To use waits and expected conditions.....
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize Base Url (The Game Catalogue Website)
BASE_URL = "https://cozy-profiterole-618935.netlify.app/"
# initializing Chrome Webdriver..
chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

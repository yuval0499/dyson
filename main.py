from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui 
import time



chrome_options = Options()
chrome_options.add_argument('--start-maximized')

browser = Chrome('C:/Users/AG23/Documents/offer/chromedriver', chrome_options=chrome_options)
browser.get('https://ofersale.ofermalls.co.il/MissTheMall/?utm_source=sms&utm_medium=sms&utm_campaign=MissTheMall')
browser.find_elements_by_xpath("//a[@href='javascript: StartGame()']")[0].click()
pyautogui.scroll(-200)
actions = ActionChains(browser)
actions.send_keys('קסו')
actions.perform();
time.sleep(0)
pyautogui.click()

actions = ActionChains(browser)
actions.send_keys('וס')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)
actions.send_keys('אד')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)

actions.send_keys('יייי')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)

actions.send_keys('מו')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)


actions.send_keys('קווביה')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)


actions.send_keys('פנור')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)


actions.send_keys('אירקיג')
actions.perform();
time.sleep(0)

pyautogui.click()

actions = ActionChains(browser)


actions.send_keys('ארי')
actions.perform();

pyautogui.click()

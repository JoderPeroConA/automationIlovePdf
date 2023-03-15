import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

print(sys.path[1])
ruth = "/chromedriver.exe"
system = sys.path[1]
path = system + ruth
print(path)

driver = None
driverWait = None
action = None

'''def init():
    print("Iniciando")
    global driver, driverWait, action
    driver = webdriver.Chrome(path)
    driverWait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.ilovepdf.com/es/pdf_a_powerpoint")
'''


def init():
    global driver
    driver = webdriver.Chrome(path)
    driver.maximize_window()
    driver.get("https://www.ilovepdf.com/es/comprimir_pdf")


def close():
    global driver
    driver.quit()

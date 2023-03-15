from automationIlovePdf.Utilities import utilities
# from automationIlovePdf.Utilities import utilities

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def send_upload_file(
        pathFileUpLoad=r"C:\Users\Rentadvisor\Documents\Consultoria RPA\Documentos Rocketbot\Bot_En_Producción.pdf"):
    bt_up = utilities.driverWait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='uploader']//input")))
    bt_up.send_keys(pathFileUpLoad)


def validation_name_file():
    sec = utilities.driverWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".file__info")))
    return sec.text()


def click_bt_convert():
    bt_convert = utilities.driverWait.until(EC.visibility_of_element_located((By.ID, "processTask")))
    utilities.action.move_to_element(bt_convert).click().perform()


def validation_bt_download():
    bt_download = utilities.driverWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".downloader")))
    return utilities.driverWait.until(EC._element_if_visible(bt_download))


def click_bt_download():
    bt_download = utilities.driverWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".downloader")))
    utilities.action.move_to_element(bt_download).click().perform()

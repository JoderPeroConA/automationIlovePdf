import time
import unittest

from automationIlovePdf.src import upload_page
from automationIlovePdf.Utilities import utilities


#from automationIlovePdf.src import upload_page
#from automationIlovePdf.Utilities import utilities

class TestUpload(unittest.TestCase):
    def setUp(self) -> None:
        print("Inicio SetUp")
        self.driver = utilities
        self.upload = upload_page

    def test_upload_file(self):
        t = 2
        # driver = self.driver
        # driverWait = self.driverWait
        # action = ActionChains(driver)

        # pathFileUpLoad = r"C:\Users\Rentadvisor\Documents\Consultoria RPA\Documentos Rocketbot/Bot_En_Producción.pdf"

        # driver.get("https://www.ilovepdf.com/es/pdf_a_powerpoint")

        # bt_up = driverWait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='uploader']//input")))
        # time.sleep(3)
        # bt_up.send_keys(pathFileUpLoad)
        self.upload.send_upload_file()

        time.sleep(t)
        # driverWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".file__info")))
        # time.sleep(t)
        self.assertEqual(self.upload.validation_name_file(), "Bot_En_Producción.pdf")
        time.sleep(t)

        # BtConvertir
        # btConvertir = driverWait.until(EC.visibility_of_element_located((By.ID, "processTask")))
        # action.move_to_element(btConvertir).click().perform()
        self.upload.click_bt_convert()
        self.assertTrue(self.upload.validation_bt_download())
        time.sleep(t)

        # BtDescarga
        # btDescarga = driverWait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".downloader")))
        self.upload.click_bt_download()

        print("Final Descarga")
        time.sleep(20)

    def tearDown(self) -> None:
        print("Cierre tearDown")
        self.driver.close()
        if __name__ == '__main__':
            unittest.main()

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        self.find(By.ID, 'username').send_keys('这是姓名2')
        self.find(By.ID, 'memberAdd_acctid').send_keys('sdfdsfd11sfds')
        self.find(By.ID, 'memberAdd_phone').send_keys('11111111112')
        self.find(By.CLASS_NAME, 'js_btn_save').click()

        sleep(3)
        self._driver.quit()
        return True

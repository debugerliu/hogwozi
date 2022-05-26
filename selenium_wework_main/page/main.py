from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.addmember import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self._driver = webdriver.Chrome(options=options)
    #     # self._driver = webdriver.Chrome()
    #     self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
    #     self._driver.implicitly_wait(3)

    def goto_add_member(self):
        # self._driver.find_element_by_xpath('//span[text()="添加成员"]').click()
        self._driver.find_element_by_xpath('//span[text()="通讯录"]').click()
        locator = (By.XPATH, '//span[text()="添加成员"]')
        self.wait_for_click(locator)
        # WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self._driver.find_element_by_xpath('//span[text()="添加成员"]').click()
        return AddMember(self._driver)

# m = Main()
# m.goto_add_member()

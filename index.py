from selenium import webdriver

from login import Login
from register import Register


class Index(object):
    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        self._driver.find_element_by_css_selector('.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        self._driver.find_element_by_css_selector('.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)



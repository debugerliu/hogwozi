from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver


class Register(object):

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        self._driver.find_element_by_id('corp_name').send_keys('企业名称')
        self._driver.find_element_by_id('manager_name').send_keys('管理员名称')
        sleep(2)
        self._driver.quit()
        return True

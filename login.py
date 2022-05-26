from selenium.webdriver.remote.webdriver import WebDriver

from register import Register


class Login(object):

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_registry(self):
        self._driver.find_element_by_css_selector('.login_registerBar_link').click()
        return Register(self._driver)

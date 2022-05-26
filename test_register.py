from index import *


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.index.goto_login().goto_registry().register()
        self.index.goto_register().register()

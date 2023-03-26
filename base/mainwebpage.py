import pytest
from selenium import webdriver

class mainclass:

    @pytest.fixture(scope="function", autouse=True)
    def configure_browser(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(25)
        self.driver.get("https://www.salary.com/")
        yield
        self.driver.quit()
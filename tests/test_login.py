import time
from selenium.webdriver.common.by import By
from base.mainwebpage import mainclass
from assertpy import assert_that
import pytest
from utilities import data_source



class Testlogin(mainclass):
    @pytest.mark.parametrize("username,password,expected_error", data_source.test_invalid_login_data)
    def test_invalid_login(self,username,password,expected_error):
        self.driver.find_element(By.ID,"gway-nav-demo").click()
        self.driver.find_element(By.ID,"sa-global-header-login-btn").click()
        self.driver.find_element(By.LINK_TEXT,"CompAnalyst").click()
        self.driver.find_element(By.ID,"loginid").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Sign In')]").click()
        error_msg=self.driver.find_element(By.ID,"sa-alert-span-msg").text
        assert_that(error_msg).is_equal_to(expected_error)
        time.sleep(5)



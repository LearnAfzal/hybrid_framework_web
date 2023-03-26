import time
from selenium.webdriver.common.by import By
from base.mainwebpage import mainclass
from assertpy import assert_that
import pytest
from utilities import data_source
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class TestAccountCreation(mainclass):
    @pytest.mark.parametrize("FirstName,LastName,Email,CreatePassword,ConfirmPassword,Country,expected_error", data_source.test_invalid_account_creation)
    def test_invalid_account_creation(self,FirstName,LastName,Email,CreatePassword,ConfirmPassword,Country,expected_error):
        actions=webdriver.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,"//a[normalize-space()='For You']")).perform()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Create an Account']").click()
        self.driver.find_element(By.ID, "firstname").send_keys(FirstName)
        self.driver.find_element(By.ID, "lastname").send_keys(LastName)
        self.driver.find_element(By.ID, "txt_regemail").send_keys(Email)
        self.driver.find_element(By.ID, "txt_newpwd").send_keys(CreatePassword)
        self.driver.find_element(By.ID, "txt_confirmedpwd").send_keys(ConfirmPassword)
        select_country=Select(self.driver.find_element(By.XPATH,"//select[@id='countrycode']"))
        select_country.select_by_value(f'{Country}')
        #self.driver.find_element(By.ID, "chk_jobalerts").click()
        self.driver.find_element(By.ID, "chk_IsTerms").click()
        # self.driver.find_element(By.XPATH, "//a[@id='register-btn']").click() -> fails to wor as expected
        cookies_msg = self.driver.find_element(By.XPATH, "//a[text()='I Accept']")
        if cookies_msg.is_displayed():
            cookies_msg.click()
        time.sleep(3)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Register Now").click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.ID, "reg_errormsg")))
        error_msg=self.driver.find_element(By.ID,"reg_errormsg").text
        print(error_msg)
        assert_that(error_msg).is_equal_to(expected_error)
        time.sleep(5)

    @pytest.mark.parametrize("FirstName,LastName,Email,CreatePassword,ConfirmPassword,Country,expected_error",data_source.test_password_criteria)
    def test_password_criteria(self,FirstName,LastName,Email,CreatePassword,ConfirmPassword,Country,expected_error):
        actions=webdriver.ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(By.XPATH,"//a[normalize-space()='For You']")).perform()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Create an Account']").click()
        self.driver.find_element(By.ID, "firstname").send_keys(FirstName)
        self.driver.find_element(By.ID, "lastname").send_keys(LastName)
        self.driver.find_element(By.ID, "txt_regemail").send_keys(Email)
        self.driver.find_element(By.ID, "txt_newpwd").send_keys(CreatePassword)
        self.driver.find_element(By.ID, "txt_confirmedpwd").send_keys(ConfirmPassword)
        select_country=Select(self.driver.find_element(By.XPATH,"//select[@id='countrycode']"))
        select_country.select_by_value(f'{Country}')
        self.driver.find_element(By.ID, "chk_IsTerms").click()
        cookies_msg = self.driver.find_element(By.XPATH, "//a[text()='I Accept']")
        if cookies_msg.is_displayed():
            cookies_msg.click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Register Now").click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@id='reg_errormsg']")))
        error_msg=self.driver.find_element(By.XPATH,"//span[@id='reg_errormsg']").text
        print(error_msg)
        assert_that(error_msg).is_equal_to(expected_error)
        time.sleep(5)



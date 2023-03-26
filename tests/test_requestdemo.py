import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from base.mainwebpage import mainclass
from selenium import webdriver
from assertpy import assert_that
import pytest
from utilities import data_source



class TestDemo(mainclass):

    @pytest.mark.parametrize("FirstName,LastName,JobTitle,CompanyName,Email,Mobile,TotalEmp,Country,HearAbout,DemoName,SuccessMsg",data_source.test_valid_request_demo)
    def test_valid_request_demo(self,FirstName,LastName,JobTitle,CompanyName,Email,Mobile,TotalEmp,Country,HearAbout,DemoName,SuccessMsg):
        self.driver.find_element(By.ID, "gway-nav-demo").click()
        self.driver.find_element(By.ID, "schedule_modal-firstname").send_keys(FirstName)
        self.driver.find_element(By.ID, "schedule_modal-lastname").send_keys(LastName)
        self.driver.find_element(By.ID, "schedule_modal-jobtitle").send_keys(JobTitle)
        self.driver.find_element(By.ID, "schedule_modal-companyname").send_keys(CompanyName)
        self.driver.find_element(By.ID, "schedule_modal-email").send_keys(Email)
        self.driver.find_element(By.ID,"schedule_modal-phonenumber").send_keys(Mobile)
        self.driver.find_element(By.ID,"schedule_modal-number").send_keys(TotalEmp)
        self.driver.find_element(By.XPATH,"//div[@id='schedule_modal-country-wrapper']").click()
        self.driver.find_element(By.XPATH,f"//span[@data-countrycode='{Country}']").click()
        self.driver.find_element(By.ID,"schedule_modal-hearabout").send_keys(HearAbout)
        cookies_msg = self.driver.find_element(By.XPATH, "//a[text()='I Accept']")
        if cookies_msg.is_displayed():
            cookies_msg.click()
        self.driver.find_element(By.XPATH,"//a[@id='schedule_modal-product_DropdownMenuBtn']").click()
        self.driver.find_element(By.XPATH, f"//span[contains(text(),'{DemoName}')]").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Confirm Products')]").click()
        # to scroll down using java-script
        """confirm_button = self.driver.find_element(By.XPATH, "//span[contains(text(),'Confirm Products')]")
        while len(self.driver.find_elements(By.XPATH,"//span[contains(text(),'Confirm Products')]"))==0:
            self.driver.execute_script("window.scrollTo(0, 500)")
        if confirm_button.is_displayed():
            confirm_button.click()"""
        time.sleep(3)
        self.driver.find_element(By.ID,"schedule-dropdownmenubtn").click()
        self.driver.find_element(By.XPATH,"//span[@class='cursor-pointer']").click()
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Confirm Time')]").click()
        self.driver.find_element(By.XPATH, "//span[text()='Submit']").click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Your request has been received.')]")))
        success_msg=self.driver.find_element(By.XPATH, "//span[contains(text(),'Your request has been received.')]").text
        print(success_msg)
        assert_that(success_msg).is_equal_to(SuccessMsg)
        time.sleep(5)

    @pytest.mark.parametrize("FirstName,LastName,JobTitle,CompanyName,Email,Mobile,TotalEmp,Country,HearAbout,DemoName,InvalidField,ErrorMsg",data_source.test_invalid_request_demo)
    def test_invalid_request_demo(self, FirstName, LastName, JobTitle, CompanyName, Email, Mobile, TotalEmp, Country,HearAbout, DemoName, InvalidField, ErrorMsg):
            self.driver.find_element(By.ID, "gway-nav-demo").click()
            self.driver.find_element(By.ID, "schedule_modal-firstname").send_keys(FirstName)
            self.driver.find_element(By.ID, "schedule_modal-lastname").send_keys(LastName)
            self.driver.find_element(By.ID, "schedule_modal-jobtitle").send_keys(JobTitle)
            self.driver.find_element(By.ID, "schedule_modal-companyname").send_keys(CompanyName)
            self.driver.find_element(By.ID, "schedule_modal-email").send_keys(Email)
            self.driver.find_element(By.ID, "schedule_modal-phonenumber").send_keys(Mobile)
            self.driver.find_element(By.ID, "schedule_modal-number").send_keys(TotalEmp)
            self.driver.find_element(By.XPATH, "//div[@id='schedule_modal-country-wrapper']").click()
            self.driver.find_element(By.XPATH, f"//span[@data-countrycode='{Country}']").click()
            self.driver.find_element(By.ID, "schedule_modal-hearabout").send_keys(HearAbout)
            cookies_msg = self.driver.find_element(By.XPATH, "//a[text()='I Accept']")
            if cookies_msg.is_displayed():
                cookies_msg.click()
            self.driver.find_element(By.XPATH, "//a[@id='schedule_modal-product_DropdownMenuBtn']").click()
            self.driver.find_element(By.XPATH, f"//span[contains(text(),'{DemoName}')]").click()
            self.driver.find_element(By.XPATH, "//span[contains(text(),'Confirm Products')]").click()
            """wait = WebDriverWait(self.driver, 30)
            wait.until(expected_conditions.visibility_of_element_located((By.ID, "schedule-dropdownmenubtn")))"""
            time.sleep(3)
            self.driver.find_element(By.ID, "schedule-dropdownmenubtn").click()
            self.driver.find_element(By.XPATH, "//span[@class='cursor-pointer']").click()
            self.driver.find_element(By.XPATH, "//span[contains(text(),'Confirm Time')]").click()
            self.driver.find_element(By.XPATH, "//span[text()='Submit']").click()
            if(InvalidField=="Work Email"):
                error_msg = self.driver.find_element(By.XPATH, "//span[text()='Please input a valid email address.']").text
                print(error_msg)
                assert_that(error_msg).is_equal_to(ErrorMsg)
            elif(InvalidField=="Total Employees"):
                error_msg = self.driver.find_element(By.XPATH,"//span[text()='Please input a valid number.']").text
                print(error_msg)
                assert_that(error_msg).is_equal_to(ErrorMsg)
            time.sleep(5)

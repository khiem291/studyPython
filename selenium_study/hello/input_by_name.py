# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TempByName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://newtours.demoaut.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_checkbox(self):
        driver = self.driver
        driver.get('https://www.facebook.com/')
        var = driver.find_element_by_name('persistent')
        print var.is_selected()
        if not var.is_selected():
            var.click()

    def kktest_temp_by_name(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com/")
#         driver.get("http://selenium.googlecode.com/svn/trunk/docs/api/java/index.html")
#         driver.switch_to_frame('classFrame')
#         driver.find_element_by_link_text('Deprecated').click()
#         time.sleep(3)
#         driver.switch_to_alert().accept()
        driver.im
        try: self.assertEqual("Welcome: Mercury Tours", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))

        '''
        web driver not support css: contains
        '''
        driver.find_element_by_css_selector('font:contains("Password:")').get_text()

        driver.find_element_by_link_text("SIGN-ON").click()
        #driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys("aloha")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()  # close all
        'or self.driver.close() only close the browser window that WebDriver is currently'
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

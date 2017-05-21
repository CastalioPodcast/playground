# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestCastalio(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://castalio.info/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_castalio(self):
        driver = self.driver
        driver.get("http://castalio.info/")
        driver.find_element_by_id("tipue_search_input").send_keys("6 anos")
        driver.find_element_by_id("tipue_search_input").send_keys(Keys.ENTER)
        driver.find_element_by_link_text(u"Episódio 88: Episódio Especial de 6 Anos").click()
        self.assertEqual(u"Episódio 88: Episódio Especial de 6 Anos - Castálio Podcast", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        self.open_home_page()
        self.login("admin", "secret")
        self.open_group_page()
        self.init_create_new_group()
        self.fill_form()
        self.submit_form()
        self.logout()

    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost:8888/addressbook/group.php")

    def login(self, username, password):
        wd = self.wd
        # Login
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_group_page(self):
        wd = self.wd
        # Open group page
        wd.find_element_by_css_selector('#nav > ul > li.admin > a').click()

    def init_create_new_group(self):
        wd = self.wd
        # init create new group
        wd.find_element_by_name("new").click()

    def fill_form(self):
        wd = self.wd
        # fill forms
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("name")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("header")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("footer")

    def submit_form(self):
        wd = self.wd
        # submit form
        wd.find_element_by_name("submit").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def tearDown(self):
        wd = self.wd
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

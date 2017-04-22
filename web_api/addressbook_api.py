from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AddressBookAPI:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost:8888/addressbook/group.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # Login
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

    def fill_form(self, group):
        wd = self.wd
        # fill forms
        if group.name is not None:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header is not None:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer is not None:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)

    def submit_form(self):
        wd = self.wd
        # submit form
        wd.find_element_by_name("submit").click()

    def create_group(self, group):
        self.init_create_new_group()
        self.fill_form(group)
        self.submit_form()

    def return_to_group_page(self):
        wd = self.wd
        # return to group page
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        # logout
        wd.find_element_by_css_selector('form[name="logout"] > a').click()

    def destroy(self):
        self.wd.quit()

    def delete_group_by_number(self, number):
        wd = self.wd
        checkboxes = wd.find_elements_by_name("selected[]")
        checkboxes[number].click()
        wd.find_element_by_name("delete").click()

    def message(self):
        wd = self.wd
        return wd.find_element_by_css_selector("div.msgbox").text

    def is_element_present(self, By, locator):
        wd = self.wd
        try:
            wd.find_element(By, locator)
            return True
        except NoSuchElementException:
            return False

    def is_group_present(self):
        self.open_group_page()
        self.is_element_present(By.NAME, "selected[]")
# -*- coding: utf-8 -*-
import unittest
from models.group.group import Group
from web_api.addressbook_api import AddressBookAPI


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.app = AddressBookAPI()
    
    def test_add_group(self):
        test_group = Group("name", "header", "footer")
        self.app.open_home_page()
        self.app.login("admin", "secret")
        self.app.open_group_page()
        self.app.init_create_new_group()
        self.app.fill_form(test_group)
        self.app.submit_form()
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()

import pytest
from models.group.group import Group
from web_api.addressbook_api import AddressBookAPI


@pytest.fixture()
def app():
    app = AddressBookAPI()
    yield app
    app.destroy()


def test_add_group(app):
    test_group = Group("name", "header", "footer")
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.init_create_new_group()
    app.fill_form(test_group)
    app.submit_form()
    #TODO verify group message
    app.logout()
    #TODO verify group in  group list

import pytest
from web_api.addressbook_api import AddressBookAPI
@pytest.fixture(scope = "session")
def app():
    app = AddressBookAPI()
    yield app
    app.destroy()

@pytest.fixture(scope = "session")
def init_login(app):
    app.login("admin", "secret")
    yield
    app.logout()
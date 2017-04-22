import pytest
from web_api.addressbook_api import AddressBookAPI
@pytest.fixture(scope = "session")
def app():
    app = AddressBookAPI()
    app.login("admin", "secret")
    yield app
    app.logout()
    app.destroy()
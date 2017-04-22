import pytest
from models.group.group import Group

@pytest.fixture
def init_group(app):
    if not app.is_group_present():
        test_group = Group(name="test")
        app.create_group(test_group)


def test_delete_group(app, init_login, init_group):
    app.open_group_page()
    app.delete_group_by_number(0)
    #Verify message
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
    #TODO Deletion group from the list

from models.group.group import Group
import pytest

test_groups = [
    Group(name = "Jo", header = "Hesd", footer = "foot"),
    Group(name = "koala", header = "koala", footer = "koa")
]
def test_add_group(app, init_login, test_group, db):
    app.group.open_group_page()
    old_groups_list = db.get_group_list()
    app.group.create(test_group)
    assert "A new group has been entered into the address book." in app.find_message()
    app.group.return_to_group_page()
    # Verifying new group presence in group list
    new_groups_list = db.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(test_group)
    assert sorted(old_groups_list) == sorted(new_groups_list)

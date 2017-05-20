from pytest_bdd import given, when, then, scenario
from models.group.group import Group
import time

@scenario("group.feature", "Add new group")
def test_add_new_group():
    pass

@given ("a group list")
def old_groups_list(db):
    return db.get_group_list()

@given ("a group list with <name>, <header>, <footer>")
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when ("I add a new group to the list")
def add_new_group(init_login, app, new_group):
    app.group.open_group_page()
    app.group.create(new_group)
    app.group.return_to_group_page()
    time.sleep(1)

@then ("a new group list is equal to the old list with the new group")
def verify_group_adding(db, old_groups_list, new_group):
    new_groups_list = db.get_group_list()
    assert len(old_groups_list) + 1 == len(new_groups_list)
    old_groups_list.append(new_group)
    assert sorted(old_groups_list) == sorted(new_groups_list)

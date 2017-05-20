from models.group.group import Group
import pytest

def test_modify_by_number(app, init_login, init_group, test_group, index):
    data_to_modify = test_group
    app.group.open_group_page()
    old_groups = app.group.get_list()
    app.group.modify_by_number(0, data_to_modify)
    assert "......" in app.find_message()
    app.group.return_to_group_page()
    new_groups = app.group.get_list()
    if data_to_modify.name is not None:
        old_groups[0].name = data_to_modify.name
    assert len(old_groups) == len(new_groups)
    assert sorted(new_groups) == sorted(old_groups)
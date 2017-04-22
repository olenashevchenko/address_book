from models.group.group import Group

def test_add_group(app, init_login):
    test_group = Group("name", "header", "footer")

    app.open_group_page()
    app.init_create_new_group()
    app.fill_form(test_group)
    app.submit_form()
    #verify group message
    assert "A new group has been entered into the address book." in app.message()
    app.return_to_group_page()
    #TODO verify group in  group list

def test_add_group_without_name():
    pass

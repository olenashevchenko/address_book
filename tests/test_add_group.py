from models.group.group import Group

def test_add_group(app):
    test_group = Group("name", "header", "footer")

    app.open_group_page()
    app.init_create_new_group()
    app.fill_form(test_group)
    app.submit_form()
    #TODO verify group message
    #TODO verify group in  group list

def test_add_group_without_name():
    pass

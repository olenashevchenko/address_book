
def test_delete_group(app, init_login):
    app.open_group_page()
    app.delete_group_by_number(0)
    #Verify message
    assert "Group has been removed." in app.message()
    app.return_to_group_page()
    #TODO Deletion group from the list

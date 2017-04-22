
def test_delete_group(app):
    app.open_group_page()
    app.delete_group_by_number(0)
    #TODO Verify message
    app.return_to_group_page()
    #TODO Deletion group from the list

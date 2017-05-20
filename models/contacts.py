class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id

    def __repr__(self):
        return "id: {}, {}, {}, {}".format(self.id, self.firstname, self.middlename, self.lastname)
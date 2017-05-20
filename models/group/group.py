class Group:
    def __init__ (self, name = None, header = None, footer = None, id = None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__ (self):
        return "{}, {}, {}, {}".format(self.id, self.name, self.header, self.footer)

    def __eq__ (self, other):
        if self.id is None or other.id is None:
            return self.name == other.name
        return self.id == other.id and self.name == other.name

    def __lt__ (self, other):
        if self.id is None:
            return False
        if other.id is None:
            return True
        else:
            return self.id<other.id
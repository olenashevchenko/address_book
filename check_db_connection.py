from db_api.addressbook_orm import AddressbookORM
from models.group.group import Group

config = {
    "host": "localhost",
    "port": 8889,
    "user": "root",
    "password": "root",
    "db": "test"
}

db = AddressbookORM(**config)

try:
    for c in db.get_contacts_in_group(Group(id='63')):
        print(c)
finally:
    pass
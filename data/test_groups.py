import random
import string
import json
import os.path
from models.group.group import Group

utf_symbols = ''.join([chr(l) for l in range(1, 0x10ffff) if chr(l).isprintable()])
cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF) if chr(l).isprintable()])
cyr_symbol_ru_uk = ''.join([chr(l) for l in range(0x0410, 0x0457) if chr(l).isprintable()])


def random_string(maxlen):
    length = random.randrange(maxlen)
    symbols = string.ascii_letters + string.digits + " "*10 + string.punctuation + cyr_symbol_ru_uk
    return ''.join([random.choice(symbols) for _ in range(length)])

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")

with open(file_name, encoding='utf8') as f:
    test_groups = [Group(**data) for data in json.load(f)]


# names = ['', 'hgvjhsdfcs', "123"]
# headers = ['', 'hgvjhsdfcs', "123"]
# footers = ['', 'hgvjhsdfcs', "123"]
#
# test_groups = [
#     Group(name=name, header=header, footer=footer)
#     for name in names
#     for header in headers
#     for footer in footers
test_groups += [
    Group(name=random_string(14), header=random_string(20), footer=random_string(50))
    for _ in range(5)
]

#names = ['', 'hgvjhsdfcs', "123"]
#headers = ['', 'hgvjhsdfcs', "123"]
#footers = ['', 'hgvjhsdfcs', "123"]

#test_groups = [
    #Group(name=name, header=header, footer=footer)
    #for name in names
    #for header in headers
    #for footer in footers
#] + [
    #Group(name=random_string(14), header=random_string(20), footer=random_string(50))
    #for _ in range(5)
#]


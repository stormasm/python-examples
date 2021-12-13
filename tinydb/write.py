from tinydb import TinyDB, Query
db = TinyDB('db.json')
db.insert({'type': 'pear', 'count': 9})
#db.all()
for item in db:
    print(item)

from tinydb import TinyDB, Query
db = TinyDB('db.json')
#db.all()
for item in db:
    print(item)

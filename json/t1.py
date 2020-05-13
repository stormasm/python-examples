import json
'''
t1 = json.dumps(['stu', {'bar': ('baz', None, 1.0, 2)},
                'rick', {'bar': ('baz', None, 1.0, 2)},
                'pete', {'bar': ('baz', None, 1.0, 2)},
                ])

print(t1)

https://www.w3schools.com/python/python_tuples.asp

this is an array of dictionaries with the key being
the symbol and the value being the tuple

t2 = json.dumps([{"b": ("apd","avy","bll")},
                 {"c": ("atvi","chtr","cmcsa")},
                 {"e": ("apa","cog","cop")},
                ])

print(t2)
'''

tup1 = ("apd","avy","bll")
tup2 = ("atvi","chtr","cmcsa")
tup3 = ("apa","cog","cop")

d1 = {}
d2 = {}
d3 = {}

d1["b"] = tup1
d2["c"] = tup2
d3["e"] = tup3

#t = [d1,d2,d3]
t = []
t.append(d1)
t.append(d2)
t.append(d3)

t2 = json.dumps(t)
print(t2)

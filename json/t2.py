import json

d = {}

d["b"] = "ball"
d["c"] = "cold"
d["e"] = "extra"

t2 = json.dumps(d)
print(t2)

td = json.loads(t2)
print(td["c"])

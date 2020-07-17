import redis

def redis_set_to_python_set(key):
    members = set()
    rset = r.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)

r = redis.Redis(host='localhost', port=6379, db=0)
r.sadd('testset','red')
r.sadd('testset','yellow')
r.sadd('testset','green')
members = r.smembers('testset')
print(type(members))
print(members)
myset = redis_set_to_python_set('testset')
print(myset)

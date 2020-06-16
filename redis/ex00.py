import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
x = r.get('foo')
print(x)
r.set(x,'baz')
x = r.get(x)
print(x)

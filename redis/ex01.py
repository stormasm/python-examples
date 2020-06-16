import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.lpush('ralph','hello')
r.lpush('ralph','foo')
r.lpush('ralph','bar')

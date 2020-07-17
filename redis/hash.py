import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def write_symbol_to_hash(rediskey,symbol,name):
    rc.hset(rediskey,symbol,name)

def get_field(key):
    name = rc.hget("testhash",key)
    name = name.decode("utf-8")
    return(name)

def redis_hash_to_python_dict(key):
    mydict = {}
    keys = rc.hkeys(key)
    for key in keys:
        key = key.decode("utf-8")
        name = get_field(key)
        mydict[key] = name
    return(mydict)

write_symbol_to_hash('testhash','aapl','apple computer')
write_symbol_to_hash('testhash','ui','ubiquiti networks')
write_symbol_to_hash('testhash','amzn','amazon')

hash = rc.hgetall('testhash')
print(type(hash))
print(hash)

print(get_field('ui'))
print(redis_hash_to_python_dict('testhash'))

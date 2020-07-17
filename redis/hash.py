import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def write_symbol_to_hash(rediskey,symbol,name):
    rc.hset(rediskey,symbol,name)

def get_symbol_name(symbol):
    name = rc.hget("testhash",symbol)
    name = name.decode("utf-8")
    return(name)

def redis_hash_to_python_dict(key):
    members = set()
    rset = r.smembers(key)
    for value in rset:
        value = value.decode("utf-8")
        members.add(value)
    return(members)

write_symbol_to_hash('testhash','aapl','apple computer')
write_symbol_to_hash('testhash','ui','ubiquiti networks')
write_symbol_to_hash('testhash','amzn','amazon')

result = rc.hgetall('testhash')
print(result)

print(get_symbol_name('ui'))

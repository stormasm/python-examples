import redis

rc = redis.Redis(host='localhost', port=6379, db=0)

def write_symbol_to_hash(rediskey,symbol,name):
    rc.hset(rediskey,symbol,name)

def get_symbol_name(symbol):
    name = rc.hget("testhash",symbol)
    name = name.decode("utf-8")
    return(name)

def redis_hash_to_python_dict(key):
    mydict = {}
    symbols = rc.hkeys(key)
    for symbol in symbols:
        symbol = symbol.decode("utf-8")
        name = get_symbol_name(symbol)
        mydict[symbol] = name
    return(mydict)

write_symbol_to_hash('testhash','aapl','apple computer')
write_symbol_to_hash('testhash','ui','ubiquiti networks')
write_symbol_to_hash('testhash','amzn','amazon')

hash = rc.hgetall('testhash')
print(type(hash))
print(hash)

print(get_symbol_name('ui'))
print(redis_hash_to_python_dict('testhash'))

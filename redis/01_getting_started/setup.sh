# https://hackersandslackers.com/redis-py-python/
# https://pypi.org/project/redis/

#####################
# 01 -> install redis
#####################
pip install redis
# or
pip install -r requirements.tx

###########################
# 02 -> create redis client
###########################
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')

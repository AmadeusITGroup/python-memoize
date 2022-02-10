# python-memoize
Based on [django-memoize](http://django-memoize.readthedocs.io/en/latest), is a memoization implementation technique used to cache functions' results with persistent storage in Redis.

This repository is a fork of django-memoization, and removes all dependencies on django, or even redis (if you implement the corresponding setter/getter/etc., also ttl system).

`memoize` uses arguments passed to the function to build a unique key to be used to keep track of cached values.

Example of use:
```python
from memoize import Memoizer
from redis import Redis
from typing import List
from itertools import chain

redis_cache = redis.Redis.from_url("redis://localhost:6379")
_memoize = Memoizer(cache)

# Declare the decorator we'll use on top of functions
# We could also use _memoize.memoize or _memoize.delete_memoized directly
persistent_cache = _memoize.memoize
delete_persistent_cache = _memoize.delete_memoized

@persistent_cache(ttl=30)
def sum(a: int, b: int) -> int:
    result = a + b
    print("Result of %s + %s = %s (without cache)" % (a, b, result))
    return result

@persistent_cache(ttl=30)
def merge_lists(*lst: List) -> List:
    result = list(set(chain(*lst)))
    print("Result %s (without cache)" % result)
    return result
```

Then, let's call them:
```python
# First call - no cache to be used
>>> sum(1, 2)
Result of 1 + 2 = 3 (without cache)
3

# Second call within 30s - cache is used
>>> sum(1, 2)
3

# With arrays
>>> merge_lists(ls_a, ls_b, ls_c)
Result [2, 3, 6, 7, 8, 9] (without cache)
[2, 3, 6, 7, 8, 9]

>>> merge_lists(ls_a, ls_b, ls_c)
[2, 3, 6, 7, 8, 9]

# Of course, if you change arguments, cache is not used
>>> merge_lists(ls_a, ls_b, ls_c, [18])
Result [2, 3, 6, 7, 8, 9, 18] (without cache)
[2, 3, 6, 7, 8, 9, 18]
```

You can see the key in redis:
```bash
$ redis-cli
127.0.0.1:6379> keys *
1) memoize:7f85ab05cddb2d3527e0bcacbf936e09e4b3e0ba564f40bf91ea5fa2393c0bfc

127.0.0.1:6379> ttl memoize:7f85ab05cddb2d3527e0bcacbf936e09e4b3e0ba564f40bf91ea5fa2393c0bfc 
(integer) 25 (25 seconds left)

127.0.0.1:6379> get memoize:7f85ab05cddb2d3527e0bcacbf936e09e4b3e0ba564f40bf91ea5fa2393c0bfc
"\x80\x03]q\x00(K\x02K\x03K\x06K\aK\bK\tK\x12e."
```

Values are serialized using `pickle`:
```python
import pickle
print(pickle.loads("\x80\x03]q\x00(K\x02K\x03K\x06K\aK\bK\tK\x12e."))
```

Will return:
```python
[2, 3, 6, 7, 8, 9, 18]
```

If edit the code, to run the tests installe the requirements and execute ``python -m pytest tests/``.
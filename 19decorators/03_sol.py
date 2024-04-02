"""
Problem 3: Cache Return Values
Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
"""

import time

def cache(func):
    cache_value = {}
    print(cache_value,"from cache")
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

# print(long_running_function(2,3),"1st...")
# print(long_running_function(2,3),"2nd...")
# print(long_running_function(2,3),"3rd...")
# print(long_running_function(3,2),"4th...")
print(long_running_function(3,20),"5th...")
print(long_running_function(4355,2550),"6th...")





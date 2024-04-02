'''
Problem 1: Timing Function Execution
Problem: Write a decorator that measures the time a function takes to execute.
'''

import time

def timer(func1):
    def wrapper(*args,**kwargs):
        start = time.time()
        result=func1(*args,**kwargs)
        end = time.time()
        print(f"{func1.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)


example_function(5)


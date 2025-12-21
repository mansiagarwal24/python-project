# Q1. Write a function that appends 1 to 1000 numbers to a list and add a decorator to that function to calculate the start and end time.
# Calculate the total time taken and print.

import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Total time taken: {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def append_nums():
    lst = []
    for i in range(1, 1000 + 1):
        lst.append(i)
    return lst

append_nums()


# Q2. Create a parameterised decorator retry that retries a function a specified number of times.
#
# 	@retry(3)
#             def may_fail(name):
#                   print(f"Hello, {name}!")


import time

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == times:
                        print("All retries exhausted!")
            return None
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")

may_fail("Mansi")


# Q3. Create a decorator validate_positive for below function that ensures the argument passed to a function is positive.
#
#           def square_root(x):
#     		return x ** 0.5

def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Argument must be positive")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5

print(square_root(25))
print(square_root(9))
# print(square_root(-4))


# 4.Create a decorator cache that caches the result of a function based on its arguments.
# @cache
# def expensive_computation(x):
#     print("Performing computation...")
#     return x * x
#
# expensive_computation(5)
# expensive_computation(5)

# Write a cache decorator for it to check if the calculation is already performed then return the result.

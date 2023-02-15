import functools

def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # dosomething...
        result = func(*args, **kwargs)
        # dosomething...
        return result
    return wrapper

@my_decorator # this replaces line 18
def add5(x):
    return x + 5


# print_name = start_end_decorator(print_name)

results = add5(10)
print(results)

print(help(add5))
print(add5.__name__)
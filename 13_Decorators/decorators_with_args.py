import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper

@start_end_decorator # this replaces line 24
def add5(x):
    return x + 5


# print_name = start_end_decorator(print_name)

results = add5(10)
print(results)

print(help(add5))
print(add5.__name__)
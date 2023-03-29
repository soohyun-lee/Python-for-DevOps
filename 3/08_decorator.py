def some_decorator(wrapped_function):
    def wrapper():
        print('Do something before calling wrapped function')
        wrapped_function()
        print('Do something after calling wrapped function')
    return wrapper

def foobat():
    print('foobat')

f = some_decorator(foobat)

f()

@some_decorator
def batfoo():
    print('batfoo')

batfoo()
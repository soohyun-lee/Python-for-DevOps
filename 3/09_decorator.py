# 데코레이터의 기본 형식
def some_decorator(wrapped_function):
    def wrapper():
        print('Do something before calling wrapped function')
        wrapped_function()
        print('Do something after calling wrapped function')
    return wrapper

# 함수를 정의한 뒤, 다른 함수의 인수로 넘겨줄 수 있음
def foobat():
    print('foobat')

f = some_decorator(foobat)

f()

# @decorater_name의 형식으로 데코레이팅해서 래핑할 함수를 지정 가능
@some_decorator
def batfoo()
    print('batfoo')

batfoo()
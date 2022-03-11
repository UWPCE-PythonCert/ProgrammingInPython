
print('importing')


def my_decorator(func):
    print('in my_decorator for: ', func.__name__)
    def inner():
        print('in inner function')
        func()
        print('in inner after decorated function')
    return inner


@my_decorator
def first_func():
    print('running first_func')

@my_decorator
def other_func():
    print('running other_func')

print('imports and loading done')

if __name__ == '__main__':
    print('run script')
    other_func()

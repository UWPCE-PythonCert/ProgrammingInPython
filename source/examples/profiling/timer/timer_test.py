import time


def timer(func):
    def timer(*args, **kwargs):
        """a decorator which prints execution time of the decorated
        function"""
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("-- executed %s in %.4f seconds" % (func.__name__, (t2 - t1)))
        return result
    return timer


@timer
def expensive_function():
    time.sleep(1)


@timer
def less_expensive_function():
    time.sleep(.02)

expensive_function()
less_expensive_function()

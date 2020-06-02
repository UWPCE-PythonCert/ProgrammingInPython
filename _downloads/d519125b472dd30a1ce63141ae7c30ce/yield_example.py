def counter():
    print('counter: starting counter')
    i = -3
    while i < 3:
        i = i + 1
        print('counter: yield', i)
        yield i

def y_range(start, stop, step=1):
    print("at the start")
    i = start
    while i < stop:
        print("about to yield")
        yield i
        print("after yield")
        i += step
    print("at end of func")

def test():
    yield 4
    yield 45
    yield 12


# if __name__ == '__main__':
#     print "the generator function:"
#     print repr(counter)
#     print "call generator function"

#     c = counter()
#     print " note that nothing printed"
#     print "the generator:"
#     print repr(c)

#     print 'iterate'
#     for item in c:
#         print 'received:', item

"""
Complete do-nothing metaclass example

It serves to show when each special method of the metaclass is called.

"""


class CoolMeta(type):
    def __new__(meta, name, bases, dct):
        print('Creating class in CoolMeta.__new__', name)
        return super().__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print('Initializing class  in CoolMeta.__init__', name)
        super().__init__(name, bases, dct)

    def __call__(cls, *args, **kw):
        print('calling CoolMeta to instantiate ', cls)
        return type.__call__(cls, *args, **kw)


class CoolClass(metaclass=CoolMeta):
    def __init__(self):
        print('And now my CoolClass object exists')


print('everything loaded, instantiate a CoolClass instance now')

foo = CoolClass()

# Demo of a contextmanager


class Context:
    """
    from Doug Hellmann, PyMOTW
    https://pymotw.com/3/contextlib/#module-contextlib
    """

    def __init__(self, handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val.args)
        print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
        return self.handle_error

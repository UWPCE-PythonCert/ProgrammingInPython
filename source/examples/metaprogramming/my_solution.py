# original class made as simple as possible
class TestClass(object):

    engine = None

    def __init__(self, config):
        self.config = config
        self.data = None

    def initialize(self):
        print('initialize data')
        self.data = 'initialized'

    def _get_engine(self):
        if not TestClass.engine:
            self.initialize()
        TestClass.engine = 'on'
        return TestClass.engine

    def get_privilege(self):
        engine = self._get_engine()
        return self.data, TestClass.engine


class MyClass(object):
    
    class __MyClass(object):
        def __init__(self, db_config):
            self.db_config = db_config
            self.data = None
            self.engine = None

        def initialize(self):
            print('initialize data')
            self.data = 'initialized'

        def _get_engine(self):
            if not self.engine:
                self.initialize()
            self.engine = 'on'
            return self.engine

    def get_privilege(self):
        engine = self._get_engine()
        return self.data, self.engine

    instance = None

    def __init__(self, db_config):
        if not MyClass.instance:
            MyClass.instance = MyClass.__MyClass(db_config)

    def __getattr__(self, name):
        return getattr(self.instance, name)


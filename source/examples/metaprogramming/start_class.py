import sqlalchemy


class AccessTable(object):

    engine = None

    def __init__(self, db_config):
        self.db_config = db_config

    def initialize(self, engine):
        """
        Set up schema if it does not already exist
        """
        self.metadata = sqlalchemy.MetaData()
        sqlalchemy.Table('access', self.metadata,
                         sqlalchemy.Column('name', sqlalchemy.String(256), primary_key=True),
                         sqlalchemy.Column('group', sqlalchemy.String(256), nullable=False),
                         sqlalchemy.Column('privilege', sqlalchemy.String(64), nullable=False),
                         sqlalchemy.Index('name', 'group', unique=True))
        self.metadata.create_all(engine)

    def _get_engine(self):
        """
        Get a connection to the sqlalchemy db engine

        If the initial connection fails, it will try again next time

        The engine connection is kept as a class variable since sqlalchemy engines are intended to be
        started once in the app's lifetime, not started up and shut down repeatedly.  So this is just
        a plain ol singleton
        """
        if not AccessTable.engine:
            AccessTable.engine = sqlalchemy.create_engine(self.db_config['engine'])

        self.initialize(AccessTable.engine)
        return AccessTable.engine

    def get_privilege(self, name, group):
        """
        Get the privilege for the given name and group
        """
        # TODO consider making self.engine a @property instead
        engine = self._get_engine()

        # TODO consider making self.metadata a @property
        # Also, I don't like how self.metadata is not initialized until _get_engine is called ... should be more
        # automatic than that
        access = self.metadata.tables['access']
        select = sqlalchemy.select([access.c.privilege]).where(sqlalchemy.sql.and_(access.c.name == name,
            access.c.group == group))
        
        # TODO handle result including case where it doesn't find any records
        _result = engine.execute(select)
        return 'readwrite'

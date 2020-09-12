from api import Wikipedia


class Definitions(object):

    @staticmethod
    def article(title):
        return Wikipedia.get_article(title)

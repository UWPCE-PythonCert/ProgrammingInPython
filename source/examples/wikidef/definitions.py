from api import Wikipedia


class Definitions:

    @staticmethod
    def article(title):
        return Wikipedia.get_article(title)

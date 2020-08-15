import unittest

from api import MissingArticleError
from definitions import Definitions


class WikiDefTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_article_success(self):
        article = Definitions.article("Robot")
        self.assertIn("mechanical", article)

    def test_missing_article_failure(self):
        missing_article_title = "!!!!!-NonExistentArticle"
        self.assertRaises(MissingArticleError, Definitions.article, missing_article_title)

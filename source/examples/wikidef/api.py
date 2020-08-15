#!/usr/bin/env python

"""
Some code for accessing the Wikipedia API
"""

# Really handy third-party module
# ``pip install requests`` if you don't already have it
import requests


class ParseError(Exception):
    pass


class MissingArticleError(Exception):
    pass


class Wikipedia:
    """
    Wikipedia API interface

    https://www.mediawiki.org/wiki/API:Main_page
    """

    # base url for the english edition of wikipedia
    api_endpoint = "http://en.wikipedia.org/w/api.php?"

    @classmethod
    def get_article(cls, title):
        """
        Return contents of article

        :param title: title of article
        """
        req_params = {'action': 'parse',
                      'format': 'json',
                      'prop': 'text',
                      'page': title}
        response = requests.get(cls.api_endpoint, params=req_params)
        json_response = response.json()

        if "error" in json_response:
            print(json_response)
            raise MissingArticleError(str(json_response["error"]["info"]))
        else:
            try:
                # limit the output, cause sometimes it is obnoxious
                contents = json_response['parse']['text']['*'][:1000]
                return contents
            except KeyError:
                raise ParseError(json_response)

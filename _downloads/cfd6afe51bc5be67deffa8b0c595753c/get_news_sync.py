#!/usr/bin/env python

"""
Regular synchronous script to see how much a given word is mentioned in the
news today

Took about 21 seconds for me.

Uses data from the NewsAPI:

https://newsapi.org

NOTE: you need to register with the web site to get a KEY.
"""
import time
import requests

WORD = "trump"

NEWS_API_KEY = "84d0483394c44f288965d7b366e54a74"

base_url = 'https://newsapi.org/v1/'


def get_sources():
    """
    Get all the english language sources of news

    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en"}
    resp = requests.get(url, params=params)
    data = resp.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("all the sources")
    print(sources)
    return sources


def get_articles(source):
    """
    https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=1fabc23bb9bc485ca59b3966cbd6ea26
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              # "sortBy": "latest", # some sources don't support latest
              "sortBy": "top",
              # "sortBy": "popular",
              }
    print("requesting:", source)
    resp = requests.get(url, params=params)
    if resp.status_code != 200:  # aiohttpp has "status"
        print("something went wrong with {}".format(source))
        print(resp)
        print(resp.text)
        return []
    data = resp.json()
    # the url to the article itself is in data['articles'][i]['url']
    titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return titles


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


start = time.time()
sources = get_sources()

art_count = 0
word_count = 0
for source in sources:
    titles = get_articles(source)
    art_count += len(titles)
    word_count += count_word('trump', titles)

print(WORD, "found {} times in {} articles".format(word_count, art_count))
print("Process took {:.0f} seconds".format(time.time() - start))

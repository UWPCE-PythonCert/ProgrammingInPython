#!/usr/bin/env python

"""
An Asynchronous version of the script to see how much a given word is
mentioned in the news today

Uses data from the NewsAPI:

https://newsapi.org
"""

import time
import asyncio
import aiohttp

NEWS_API_KEY = "84d0483394c44f288965d7b366e54a74"

WORD = "war"
base_url = 'https://newsapi.org/v1/'


# This has to run first, so doesn't really need async
# but why use two requests libraries ?
async def get_sources(sources):
    """
    Get all the english language sources of news

    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en", "apiKey": NEWS_API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            data = await resp.json()
            print("Got the sources")
    sources.extend([src['id'].strip() for src in data['sources']])


async def get_articles(source):
    """
    download the info for all the articles
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top"
              }
    print("requesting:", source)
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, params=params) as resp:
            if resp.status != 200:  # aiohttpp has "status"
                print(f'something went wrong with: {source}')
                await asyncio.sleep(0)  # releases control the the mainloop
                return
            # awaits response rather than waiting on response in the requests version of this
            print("got the articles from {}".format(source))
            data = await resp.json()
    # the url to the article itself is in data['articles'][i]['url']
    titles.extend([(str(art['title']) + str(art['description']))
                   for art in data['articles']])


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


start = time.time()

# start up a loop:
loop = asyncio.get_event_loop()

# create the objects to hold the data
sources = []
titles = []

# get the sources -- this is essentially synchronous
loop.run_until_complete(get_sources(sources))

# run the loop for the articles
jobs = asyncio.gather(*(get_articles(source) for source in sources))
loop.run_until_complete(jobs)
loop.close()

art_count = len(titles)
word_count = count_word(WORD, titles)

print(f'found {WORD}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')

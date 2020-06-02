#!/usr/bin/env python

"""
Gathering statistics on NBA players with the regular old
synchronous requests library.

It took: 214.62 seconds (3.6 minutes) on my machine at home on May 29th

Borrowed from:

http://terriblecode.com/blog/asynchronous-http-requests-in-python/
"""

import requests
import json
import time

base_url = 'http://stats.nba.com/stats'
HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}


def get_players(player_args):
    """
    get the names of all the players we are interested in

    This request will get JSON of the players for the 2016-17 season:

    http://stats.nba.com/stats/commonallplayers?LeagueID=00&season=2016-17&isonlycurrentseason=1

    """
    endpoint = '/commonallplayers'
    params = {'leagueid': '00',
              'season': '2016-17',
              'isonlycurrentseason': '1'}
    url = base_url + endpoint
    print('Getting all players...')
    resp = requests.get(url,
                        headers=HEADERS,
                        params=params)
    data = resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_player(player_id, player_name):
    """
    The request for a player's stats.

    Should be a request like:

    http://stats.nba.com/stats/commonplayerinfo?playerid=203112
    """
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = base_url + endpoint
    print("Getting player", player_name, player_id)
    resp = requests.get(url,
                        headers=HEADERS,
                        params=params)
    print(resp)
    data = resp.json()
    all_players[player_name] = data

all_players = {}
players = []

start = time.time()
get_players(players)

print("there are {} players".format(len(players)))
for id, name in players:
    get_player(id, name)

print("Done getting data: it took {:.2F} seconds".format(time.time() - start))

# write it out to a file
with open("NBA_stats.json", 'w') as outfile:
    json.dump(all_players, outfile, indent=2)

print("File written out")


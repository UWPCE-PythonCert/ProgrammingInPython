#!/usr/bin/env python

"""
Gathering statistics on NBA players asynchronously with the

aiohttp library

Running this on my machine, on my home network, took:


***NOTE***
On my OS-X box, a regular user is limited to 256 open files per process.
A socket is considered a file -- so this can crash out when it hits that limit.

(as of now, there are 491 players listed)

You can increase it with:

ulimit -n 2048

And see what it's set to with:

ulimit -a
***********

Borrowed from:

http://terriblecode.com/blog/asynchronous-http-requests-in-python/
"""
import pdb
import asyncio
import aiohttp
import json
import time
import requests

base_url = 'http://stats.nba.com/stats'

HEADERS = {
    'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/45.0.2454.101 Safari/537.36'),
}

# # this needs to be run first before we can start -- so no need for async
# # but making it async so we can use the aiohttp lib.
# async def get_players(players):
#     """
#     get the names of all the players we are interested in

#     This request will get JSON of the players for the 2016-17 season:

#     http://stats.nba.com/stats/commonallplayers?LeagueID=00&season=2016-17&isonlycurrentseason=1
#     """
#     endpoint = '/commonallplayers'
#     params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
#     url = base_url + endpoint
#     print('Getting all players...')
#     async with aiohttp.ClientSession() as session:
#         print("got the session")
#         async with session.get(url, headers=HEADERS, params=params) as resp:
#             print("got the response")
#             data = await resp.json()
#     players.append([(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


def get_players(player_args):
    """
    get the names of all the players we are interested in

    This request will get JSON of the players for the 2016-17 season:

    http://stats.nba.com/stats/commonallplayers?LeagueID=00&season=2016-17&isonlycurrentseason=1

    """
    endpoint = '/commonallplayers'
    params = {'leagueid': '00', 'season': '2016-17', 'isonlycurrentseason': '1'}
    url = base_url + endpoint
    print('Getting all players...')
    print("about to make request")
    resp = requests.get(url, headers=HEADERS, params=params)
    print("got the response")
    data = resp.json()
    player_args.extend(
        [(item[0], item[2]) for item in data['resultSets'][0]['rowSet']])


# this is what we want to make concurrent
async def get_player(player_id, player_name):
    endpoint = '/commonplayerinfo'
    params = {'playerid': player_id}
    url = base_url + endpoint
    print("Getting player", player_name)
    async with aiohttp.ClientSession() as session:
        print("session created")
        async with session.get(url,
                               skip_auto_headers=["User-Agent"],
                               headers=HEADERS,
                               params=params) as resp:
            print("response:", resp)
            all_players[player_name] = await resp.json()
            print("got:", player_name)
    print("Done with get_player:", player_name)

# async def get_all_stats(players):
#     for id, name in players:
#         print("getting:", name)
#         all_players[name] = await get_player(id, name)

all_players = {}
players = []

start = time.time()
loop = asyncio.get_event_loop()

print("getting the players")
# loop.run_until_complete(get_players(players))

get_players(players)
print("got the players")
print("there are {} players".format(len(players)))

# print("getting the stats")
# loop.run_until_complete(get_all_stats(players[:200]))
# print("got the stats")

loop.run_until_complete(asyncio.gather(
                     *(get_player(*args) for args in players[:10])
                     )
                    )

# loop.run_until_complete(get_player(*players[0]))

# for id, name in players:
#     all_players[name] = get_player(id, name)

print("Done getting data: it took {:.2F} seconds".format(time.time() - start))

# write it out to a file
with open("NBA_stats_2.json", 'w') as outfile:
    json.dump(all_players, outfile, indent=2)

print("File written out")

"""
    Most of the code in here was taken from https://www.mediawiki.org/wiki/API:Links the purpose of this program is to
    take the https://terraria.gamepedia.com/List_of_weapons web page and scrap it for links and saves them to a JSON
    file. The links are then queried to see if they have the 'Weapon items' category if they do then they are saved to
    the weaponlist.txt file which will later be used to get weapon stats.

    Ok so note to everyone. This code file has gotten out of hand. The purpose well still the same has gotten more
    complex then I thought it would. This is currently set up to require a bot username and password to be entered in
    PARAMS_1 but if you remove everything from lines 24 to 52 then you will be able to use the program but will ONLY be
    given 500 results per query where as bot accounts get 5000 results per query so its advised that you attempt to make
    your own bot account.
"""


import requests

file = open('weaponlist.txt', 'a')

S = requests.Session()

URL = 'https://terraria.gamepedia.com/api.php'


# Retrieve login token first
PARAMS_0 = {
    'action': "query",
    'meta': "tokens",
    'type': "login",
    'format': "json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print(LOGIN_TOKEN)

# Send a post request to login.
PARAMS_1 = {
    'action':"login",
    'lgname':"Bot username",
    'lgpassword':"Bot password",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}


R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)

PARAMS_3 = {
    'action': 'query',
    'format': 'json',
    'titles': 'List_of_weapons',
    'prop': 'links',
    'pllimit': 'max'
}

R = S.get(url=URL, params=PARAMS_3)
DATA = R.json()
print(DATA)
PAGES = DATA['query']['pages']

for k, v in PAGES.items():
    for l in v['links']:
        file.write(f"{l['title']}\n")
        print(l['title'])

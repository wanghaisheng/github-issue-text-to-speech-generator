import requests
from . import RedditUtils as utils
import json

__headers = {}

def startSession():
    global __headers
    auth = requests.auth.HTTPBasicAuth(utils.appID, utils.secretKey)
    data = {'grant_type': 'password',
            'username': utils.username,
            'password': utils.password}

    headers = {'User-Agent': 'MyBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    __headers = {**__headers, **{'Authorization': f"bearer {TOKEN}"}}

def getPosts():
    requests.get('https://oauth.reddit.com/api/v1/me', headers=__headers)
    res = requests.get("https://oauth.reddit.com/r/askReddit/hot", headers=__headers)
    with open('filename.txt', 'w') as handle:
        handle.write(json.dumps(res.json(), indent=4, sort_keys=True))
        print(json.dumps(res.json(), indent=4, sort_keys=True))

from . import RedditUtils as utils
import requests
import json
import praw

reddit = ""


def startSession():
    global reddit
    reddit = praw.Reddit(
        client_id=utils.appID,
        client_secret=utils.secretKey,
        user_agent='MyBot/0.0.1',
        username=utils.username,
        password=utils.password,
    )

    # auth = requests.auth.HTTPBasicAuth(utils.appID, utils.secretKey)
    # data = {'grant_type': 'password',
    #         'username': utils.username,
    #         'password': utils.password}
    #
    # headers = {'User-Agent': 'MyBot/0.0.1'}
    # res = requests.post('https://www.reddit.com/api/v1/access_token',
    #                     auth=auth, data=data, headers=headers)
    # TOKEN = res.json()['access_token']
    # __headers = {**__headers, **{'Authorization': f"bearer {TOKEN}"}}

def getPosts():
    subreddit = reddit.subreddit("askReddit")

    for submission in subreddit.hot(limit=10):
        print(submission.title)
        print(submission.num_comments)
        print(submission.comments)
        print("-----------")
        break


    # requests.get('https://oauth.reddit.com/api/v1/me', headers=__headers)
    # res = requests.get("https://oauth.reddit.com/r/askReddit/hot", headers=__headers)
    # data = json.loads(res.json())
    # jsonPosts = data["data"]["children"]
    # posts = []
    #
    # for jsonPost in jsonPosts:
    #     posts.append(utils.RedditPostTopic(id=jsonPost["id"],
    #                                        url=jsonPost["url"],
    #                                        subredditName=jsonPost["subreddit_name_prefixed"],
    #                                        author=jsonPost["author"],
    #                                        title=jsonPost["title"],
    #                                        upvotes=jsonPost["ups"],
    #                                        commentsCount=jsonPost["num_comments"]))
    # print("post count {}".format(len(posts)))
    # return  posts
    # with open('filename.txt', 'w') as handle:
    #     handle.write(json.dumps(res.json(), indent=4, sort_keys=True))
    #     print(json.dumps(res.json(), indent=4, sort_keys=True))

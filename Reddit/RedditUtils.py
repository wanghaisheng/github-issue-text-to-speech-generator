secretKey = "O4066063pSVpiG4GPGsaeUmxLbPK6Q"
appID = "u9vnfS4l7qrjnl_w7mOzSg"
username = "Accomplished_Fan1418"
password = "d3f0cb84e9"

from dataclasses import dataclass

@dataclass
class RedditPost:
    id: str
    title: str

@dataclass
class RedditPostToptic:
    id: str
    url: str
    subredditName: str
    author: str
    title: str
    content: str
    upvotes: int
    commentsCount: int
    posts: list[RedditPost]
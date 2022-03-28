import os

from Reddit import RedditService
from VideoCreator.speechToVoiceService import SpeechToVoiceService
from VideoCreator.screenshotService import ScreenshotService
from VideoCreator.utils import mkdirIfDoesntExist
from VideoCreator.videoEdditingService import clipTogether
from dbManager import DBManager
from moviepy.editor import *

screenshotService = None
speechToVoiceService = None
db: DBManager = None

def makeVideoFrom(submission):
    global db

    folderPath = "./VideoCreator/videos/new/askReddit_{}".format(submission.id)
    mkdirIfDoesntExist(folderPath)
    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)
    clipTogether("./VideoCreator/videos/new", submission)
    db.insertPost(submission)


def makePostVideoAt(path, submission):
    mkdirIfDoesntExist(path)

    screenshotService.screenshotPostAt(path+"/screenshot", submission)
    speechToVoiceService.makeVoiceAt(path+"/speech", submission.title)


def makeCommentsVideosAt(path, submission):
    global db

    mkdirIfDoesntExist(path)
    maxCommentCount = 30
    minimumCommentScore = 250
    maxDuration = 70

    commentPerPostCount = 0
    overallDuration = 0

    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        print(f"asd submission {submission.id}  {submission.title}  {submission.name}   comment {comment.id}")
        if commentPerPostCount >= maxCommentCount or overallDuration >= maxDuration:
            break

        if comment.score > minimumCommentScore:
            print("count is {}".format(commentPerPostCount))
            commentPerPostCount += 1
            screenshotService.screenshotCommentAt(path+"/screenshot{}".format(commentPerPostCount), comment)
            speechToVoiceService.makeVoiceAt(path+"/speech{}".format(commentPerPostCount), str(comment.body))
            overallDuration += AudioFileClip(path + f"/speech{commentPerPostCount}.mp3").duration
            db.insertComment(comment, submission.id)


def main():
    global screenshotService, speechToVoiceService, db
    submissionsLimit = 30
    minumumCommentsNumber = 1000
    minimumScore = 2000

    RedditService.startSession()
    submissions = RedditService.getHotSubmissions(limit=submissionsLimit)
    screenshotService = ScreenshotService()
    speechToVoiceService = SpeechToVoiceService()
    db = DBManager()

    madeSubmissionCount = 0
    for submission in submissions:
        if submission.num_comments > minumumCommentsNumber and submission.score > minimumScore and db.getPostWithId(post_id=submission.id) is None and madeSubmissionCount <= 6:
            makeVideoFrom(submission)
            madeSubmissionCount += 1

if __name__ == '__main__':
    main()




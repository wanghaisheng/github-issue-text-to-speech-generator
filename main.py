from Reddit import RedditService
import speechToVoiceService
import screenshotService
import os


def mkdirIfExists(path):
    if os.path.isdir(path):
        print("path {} exists".format(path))
        return
    else:
        os.mkdir(path)  # new directory


def makeVideoFrom(submission):
    folderPath = "./videos/new/askReddit_{}".format(submission.id)
    mkdirIfExists(folderPath)
    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)


def makePostVideoAt(path, submission):
    mkdirIfExists(path)

    screenshotService.screenshotPostAt(path, submission)
    speechToVoiceService.makeVoiceAt(path, submission.title)
    clipTogether(path)


def makeCommentsVideosAt(path, submission):
    mkdirIfExists(path)
    commentPerPostCount = 0
    for comment in submission.comments:
        if comment.score > 1000 and commentPerPostCount <= 10:
            commentPerPostCount += 1
            screenshotService.screenshotCommentAt(path, comment)
            speechToVoiceService.makeVoiceAt(path, comment)


def clipTogether(path):
    pass

if __name__ == '__main__':
    RedditService.startSession()
    submissions = RedditService.getHotSubmissions()
    for submission in submissions:
        if submission.num_comments > 2000 and submission.score > 5000:
            print("saving submisiion")
            makeVideoFrom(submission)
    # speechToVoiceService.makeVoiceAt("./videos/new/askReddit_{}".format("skzwrs"), "What is a socially unacceptable thing that you dont like or hate")
    # screenshotService.screenshotPostAt("./videos/new/askReddit_{}".format("skzwrs"), "asd")
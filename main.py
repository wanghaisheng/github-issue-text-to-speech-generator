from Reddit import RedditService
from speechToVoiceService import SpeechToVoiceService
from screenshotService import ScreenshotService
from utils import mkdirIfExists
from videoEdditingService import clipTogether

screenshotService = None
speechToVoiceService = None

def makeVideoFrom(submission):
    folderPath = "./videos/new/askReddit_{}".format(submission.id)
    mkdirIfExists(folderPath)
    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)
    clipTogether(folderPath)


def makePostVideoAt(path, submission):
    mkdirIfExists(path)

    screenshotService.screenshotPostAt(path+"/screenshot", submission)
    speechToVoiceService.makeVoiceAt(path+"/speech", submission.title)


def makeCommentsVideosAt(path, submission):
    mkdirIfExists(path)
    commentPerPostCount = 0

    for comment in submission.comments.list():
        if commentPerPostCount >= 5:
            break

        if comment.score > 500:
            print("count is {}".format(commentPerPostCount))
            commentPerPostCount += 1
            screenshotService.screenshotCommentAt(path+"/screenshot{}".format(commentPerPostCount), comment)
            speechToVoiceService.makeVoiceAt(path+"/speech{}".format(commentPerPostCount), str(comment.body))

def main():
    global screenshotService, speechToVoiceService

    RedditService.startSession()
    submissions = RedditService.getHotSubmissions()
    screenshotService = ScreenshotService()
    speechToVoiceService = SpeechToVoiceService()

    for submission in submissions:
        if submission.num_comments > 2000 and submission.score > 5000:
            makeVideoFrom(submission)

if __name__ == '__main__':
    main()
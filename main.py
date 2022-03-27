from Reddit import RedditService
from VideoCreator.speechToVoiceService import SpeechToVoiceService
from VideoCreator.screenshotService import ScreenshotService
from VideoCreator.utils import mkdirIfExists
from VideoCreator.videoEdditingService import clipTogether
from dbManager import DBManager

screenshotService = None
speechToVoiceService = None
db: DBManager = None

def makeVideoFrom(submission):
    global db

    folderPath = "./VideoCreator/videos/new/askReddit_{}".format(submission.id)
    mkdirIfExists(folderPath)
    db.insertPost(submission)
    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)
    clipTogether(folderPath)


def makePostVideoAt(path, submission):
    mkdirIfExists(path)

    screenshotService.screenshotPostAt(path+"/screenshot", submission)
    speechToVoiceService.makeVoiceAt(path+"/speech", submission.title)


def makeCommentsVideosAt(path, submission):
    global db

    mkdirIfExists(path)
    commentPerPostCount = 0

    for comment in submission.comments.list():
        print(f"asd submission {submission.id}  {submission.title}  {submission.name}   comment {comment.id}")
        if commentPerPostCount >= 5:
            break

        if comment.score > 500:
            print("count is {}".format(commentPerPostCount))
            commentPerPostCount += 1
            screenshotService.screenshotCommentAt(path+"/screenshot{}".format(commentPerPostCount), comment)
            speechToVoiceService.makeVoiceAt(path+"/speech{}".format(commentPerPostCount), str(comment.body))
            db.insertComment(comment, submission.id)

def main():
    global screenshotService, speechToVoiceService, db

    RedditService.startSession()
    submissions = RedditService.getHotSubmissions()
    screenshotService = ScreenshotService()
    speechToVoiceService = SpeechToVoiceService()
    db = DBManager()

    for submission in submissions:
        if submission.num_comments > 2000 and submission.score > 5000 and db.getPostWithId(post_id=submission.id) is None:
            print(f"asd getPostWithId {db.getPostWithId(post_id=submission.id)}")
            makeVideoFrom(submission)

if __name__ == '__main__':
    main()




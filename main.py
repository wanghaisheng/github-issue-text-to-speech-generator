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
    if os.path.isdir(folderPath):
        print("path {} exists, something is wrong".format(folderPath))
        return
    else:
        os.mkdir(folderPath)  # new directory
        print("creating new directory {}".format(folderPath))

    makePostVideoAt(folderPath + "/post", submission)
    makeCommentsVideosAt(folderPath + "/comments", submission)


def makePostVideoAt(path, submission):
    mkdirIfExists(path)

    screenshotService.screenshotPostAt(path, submission)
    speechToVoiceService.makeVoiceAt(path, submission.title)
    # clipTogether(screenshot, voice)


def makeCommentsVideosAt(path, submission):
    mkdirIfExists(path)
    pass


if __name__ == '__main__':
    pass
    # RedditService.startSession()
    # submissions = RedditService.getHotSubmissions()
    # for submission in submissions:
    #     if submission.num_comments > 2000 and submission.score > 5000:
    #         print("saving submisiion")
    #         makeVideoFrom(submission)
    # speechToVoiceService.makeVoiceAt("./videos/new/askReddit_{}".format("skzwrs"), "What is a socially unacceptable thing that you dont like or hate")
    screenshotService.screenshotPostAt("./videos/new/askReddit_{}".format("skzwrs"), "asd")
from Reddit import RedditService
from speechToVoiceService import SpeechToVoiceService
from screenshotService import ScreenshotService
from moviepy.editor import *
from moviepy.video.fx.crop import crop
import os

screenshotService = None
speechToVoiceService = None

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


def clipTogether(path):
    bgVidoPath = "./videos/bgVideos/video1.mp4"

    bgClip = VideoFileClip(bgVidoPath)
    (w, h) = bgClip.size
    cropedBgClip = crop(bgClip, width=1080, height=1920, x_center=w/2, y_center=h/2)
    finalBgClip = concatenate_videoclips([cropedBgClip])
    # ffmpeg command for creating post video
    os.system('ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -c:a aac -b:a '
              '192k -pix_fmt yuv420p {}'.format(path + "/post/screenshot.jpg", path + "/post/speech.mp3", path + "/post/out.mp4"))

    for fileName in os.listdir(path + "/comments"):
        if fileName.endswith(".jpg"):
            count = fileName.removeprefix("screenshot").removesuffix(".jpg")

            if os.path.isfile(path + "/comments/speech{}.mp3".format(count)):
                print("is file")
                os.system(
                    'ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -c:a aac -b:a '
                    '192k -pix_fmt yuv420p {}'.format(path + "/comments/screenshot{}.jpg".format(count), path + "/comments/speech{}.mp3".format(count),
                                                      path + "/comments/out{}.mp4".format(count)))

    print("asd clip together")
    # final = CompositeVideoClip(finalBgClip)
    # final.write_videofile("./videos/concat.mp4")

if __name__ == '__main__':
    RedditService.startSession()
    submissions = RedditService.getHotSubmissions()
    screenshotService = ScreenshotService()
    speechToVoiceService = SpeechToVoiceService()

    for submission in submissions:
        if submission.num_comments > 2000 and submission.score > 5000:
            makeVideoFrom(submission)
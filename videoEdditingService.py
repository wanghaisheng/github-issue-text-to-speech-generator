import os
from utils import mkdirIfExists
from moviepy.editor import *
from moviepy.video.fx.crop import crop
import subprocess


def clipTogether(path):
    mkdirIfExists(path + "/videos")

    # ffmpeg command for creating post video
    clips = []
    postVideoPath = path + "/videos/out.mp4"
    os.system(
        'ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -b:v 1M -c:a aac -b:a '
        '192k -pix_fmt yuv420p {}'.format(path + "/post/screenshot.jpg", path + "/post/speech.mp3", postVideoPath))
    clips.append(VideoFileClip(postVideoPath))

    # ffmpeg creating comments videos
    for fileName in os.listdir(path + "/comments"):
        if fileName.endswith(".jpg"):
            count = fileName.removeprefix("screenshot").removesuffix(".jpg")

            if os.path.isfile(path + "/comments/speech{}.mp3".format(count)):
                commentVideoPath = path + "/videos/out{}.mp4".format(count)
                os.system(
                    'ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -b:v 1M -c:a aac -b:a '
                    '192k -pix_fmt yuv420p {}'.format(path + "/comments/screenshot{}.jpg".format(count),
                                                      path + "/comments/speech{}.mp3".format(count),
                                                      commentVideoPath))
                clips.append(VideoFileClip(commentVideoPath))

    for i in range(0, len(clips)):
        clips[i] = clips[i].set_position("center")
        clips[i] = clips[i].resize(width=1000)
        if i == 0:
            clips[i] = clips[i].set_start(0)
            clips[i] = clips[i].set_end(clips[i].duration)
        else:
            clips[i] = clips[i].set_start(clips[i - 1].end)
            clips[i] = clips[i].set_end(clips[i].start + clips[i].duration)

    finalBgClip = getBgClipForClips(clips)

    clips.insert(0, finalBgClip)
    final_clip = CompositeVideoClip(clips)
    final_clip.write_videofile(path + "/videos/output_1.mp4", temp_audiofile=path + "/videos/temp-audio.m4a",
                               remove_temp=True, codec="libx264",
                               audio_codec="aac")


def getBgClipForClips(clips: [VideoFileClip]):
    bgVideo = VideoFileClip("./videos/bgVideos/video1.mp4")
    (w, h) = bgVideo.size
    croppedBgClip = crop(bgVideo, width=1080, height=1920, x_center=w / 2, y_center=h / 2)

    overallDuration = 0

    for clip in clips:
        overallDuration += clip.duration

    intDevision = overallDuration // croppedBgClip.duration
    remnant = overallDuration / croppedBgClip.duration - intDevision

    remnantSubclip = croppedBgClip.subclip(0, croppedBgClip.duration * remnant)
    croppedClips = [croppedBgClip] * int(intDevision)
    croppedClips.insert(0, remnantSubclip)

    return concatenate_videoclips(croppedClips)

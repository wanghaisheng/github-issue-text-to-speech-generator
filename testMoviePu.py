from moviepy.editor import *
from moviepy.video.fx.crop import crop

path = "./videos/new/askReddit_thnmmc/videos/"
clip = VideoFileClip(path + "out1.mp4")
clip2 = VideoFileClip(path + "out2.mp4")
clip3 = VideoFileClip(path + "out3.mp4")
clip4 = VideoFileClip(path + "out4.mp4")
clip5 = VideoFileClip(path + "out5.mp4")

clips = [clip, clip2, clip3, clip4, clip5]

for i in range(0, len(clips)):
    clips[i] = clips[i].set_position("center")
    clips[i] = clips[i].resize(width=1000)
    clips[i] = clips[i].fx(vfx.speedx, 1.1)
    if i == 0:
        clips[i] = clips[i].set_start(0)
        clips[i] = clips[i].set_end(clips[i].duration)
    else:
        clips[i] = clips[i].set_start(clips[i - 1].end)
        clips[i] = clips[i].set_end(clips[i].start + clips[i].duration)



bgVideo = VideoFileClip("./videos/bgVideos/video1.mp4")
(w, h) = bgVideo.size
cropedBgClip = crop(bgVideo, width=1080, height=1920, x_center=w/2, y_center=h/2)
finalBgClip = concatenate_videoclips([cropedBgClip])
#
clips.insert(0, cropedBgClip)
final_clip = CompositeVideoClip(clips)
final_clip.write_videofile("output_1.mp4", temp_audiofile='temp-audio.m4a', remove_temp=True, codec="libx264", audio_codec="aac")

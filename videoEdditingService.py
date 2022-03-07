import os
from utils import mkdirIfExists


def clipTogether(path):
    mkdirIfExists(path + "/videos")
    bgVideoPath = "./videos/bgVideos/video1.mp4"
    os.system("touch {}".format(path + "/videos/videos.txt"))
    file = open(path + "/videos/videos.txt", 'w')

    # bgClip = VideoFileClip(bgVidoPath)
    # (w, h) = bgClip.size
    # cropedBgClip = crop(bgClip, width=1080, height=1920, x_center=w/2, y_center=h/2)
    # finalBgClip = concatenate_videoclips([cropedBgClip])
    # ffmpeg command for creating post video
    os.system('ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -b:v 1M -c:a aac -b:a '
              '192k -pix_fmt yuv420p {}'.format(path + "/post/screenshot.jpg", path + "/post/speech.mp3", path + "/videos/out.mp4"))
    file.write("file 'out.mp4'\n")

    # ffmpeg creating comments videos
    for fileName in os.listdir(path + "/comments"):
        if fileName.endswith(".jpg"):
            count = fileName.removeprefix("screenshot").removesuffix(".jpg")

            if os.path.isfile(path + "/comments/speech{}.mp3".format(count)):
                print("is file")
                os.system(
                    'ffmpeg -i {} -i {} -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -tune stillimage -b:v 1M -c:a aac -b:a '
                    '192k -pix_fmt yuv420p {}'.format(path + "/comments/screenshot{}.jpg".format(count), path + "/comments/speech{}.mp3".format(count),
                                                      path + "/videos/out{}.mp4".format(count)))
                file.write("file 'out{}.mp4'\n".format(count))
    file.close()

    ## concatinating the post and comment videos together
    os.system("ffmpeg -f concat -safe 0 -i {}/videos/videos.txt -vf select=concatdec_select -vf 'pad=ceil(iw/2)*2:ceil(ih/2)*2' -vf scale=1000:-1 -af aselect=concatdec_select,aresample=async=1 {}/videos/finalOutput.mp4".format(path, path))

    ## cropping the bg video
    os.system("ffmpeg -i {} -filter:v 'crop=1080:1920:in_w/2 - 1080/2:in_h /2 - 1920/2' {}croppedBg.mp4".format(bgVideoPath, path + "/videos/"))

    ## overlay command
    os.system("""ffmpeg -i {} -i {} \
                -filter_complex "[0:v][1:v] overlay=(W-w)/2:(H-h)/2:enable='between(t,0,t)'" \
                -pix_fmt yuv420p -c:a copy \
                {}
                """.format(path + "/videos/croppedBg.mp4", path + "/videos/finalOutput.mp4", path + "/videos/readyVideo.mp4"))

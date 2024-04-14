from sys import argv
from pytube import YouTube
import moviepy.editor as mpe
import os
import shutil

def downloader(link):
    vname="clip.mp4"
    aname="audio.mp3"
    yt=YouTube(link)
    title=yt.title
    print("Title :",yt.title)
    print("Views :",yt.views )


    video = yt.streams.filter(subtype='mp4', res='1080p').first().download()
    os.rename(video,vname)

    audio=yt.streams.filter(only_audio=True).first().download()
    os.rename(audio,aname)


    video=mpe.VideoFileClip(vname)
    audio=mpe.AudioFileClip(aname)
    final=video.set_audio(audio)


    final.write_videofile(f"{title}.mp4",codec="libx264")
    os.remove(vname)
    os.remove(aname)

    shutil.move(f"{title}.mp4", "/home/manmohan/Documents/videos")


if __name__=="__main__":
    link= argv[1]
    downloader(link)


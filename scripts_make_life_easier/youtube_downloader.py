from sys import argv
from pytube import YouTube
import moviepy.editor as mpe
import os
import shutil

vname="clip.mp4"
aname="audio.mp3"
link= argv[1]
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
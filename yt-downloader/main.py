from pytube import YouTube
from pytube.cli import on_progress
import ffmpeg
import requests
a = input("Введите ссылку для скачивания:")
yt = YouTube(a)
#print(yt.streams)
#yt.streams.filter(file_extension = 'mp4')
stream = yt.streams.get_by_itag(22)
stream.download()
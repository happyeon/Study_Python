# -*- coding:utf-8 -*-

# pip install pytube3

from pytube import YouTube
from glob import glob
from os import path, mkdir, rename

tartget_url = input('download url : ')
download_path = 'c:/download/'

if not path.exists(download_path):
    mkdir(download_path)
    print('mkdir : ' + download_path)
else:
    print('exists')


target = YouTube(tartget_url)


# 에러 났을 때 예외 호출
try:
    target.streams.filter(only_audio=True).first().download(download_path)
    print('download success')
except:
    print('download failed')


rename(glob(download_path + '/*.mp4')[0], download_path + "/" + target.title.replace('/', '_') + '.mp3')
print('end')
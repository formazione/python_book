

from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=NWIQCDtWyjA")
print(yt.title)
stream = yt.streams.first()
stream.download() # this will download in your current working Dir
# Improvements required
# Enter video URL, Choose store path, set file name, choose resolution...

from pytube import YouTube

Download_PATH = "F:/"

#user_link = input("Enter video link: ") #link opens on opening
link = "https://www.youtube.com/watch?v=7dxwJTSDb8c"

#user_filename = input("Enter video name: ")

#creating object
yt = YouTube(link) # 'url_encoded_fmt_stream_map'
# refer https://github.com/nficano/pytube/pull/534/commits/e5f1a9e2476b096ed2012939d50851d3499016e1

#mp4files = yt.filter('mp4') #AttributeError: 'YouTube' object has no attribute 'filter'

#yt.set_filename(yt.title) #err

yt.streams.all()
stream = yt.streams.first()
stream.download()

print("Done")
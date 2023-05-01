from yt_dlp import YoutubeDL
import youtubesearchpython
import threading

class Downloader(threading.Thread):
    def __init__(self, set_folder) -> None:
        super().__init__()
        self.status_ = 'idle'
        self.set_folder = set_folder

    def search(self, search_str):
        self.links = []
        self.titles = []
        self.durations = []
        self.status_ = 'searching'
        print('searching')
        search = youtubesearchpython.VideosSearch(search_str, limit=10)
        self.result = search.result()['result']
        self.status_ = 'idle'
    
    def download(self, link, name):
        options = {
            'outtmpl': f'{self.set_folder}/{name}.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        }
        with YoutubeDL(options) as ydl:
            self.status_ = 'downloading'
            ydl.download(link)
            self.status_ = 'idle'

    @property
    def status(self):
        return self.status_
    
    @property
    def retrive(self):
        data = []
        for i in self.result:
            data.append(dict(link = i['link'], title = i['title'], duration = i['duration']))
        return data


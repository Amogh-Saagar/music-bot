import tkinter
import os
import math
import time
import threading

def convertMillis(frames, freq):
    seconds = math.floor(frames/freq)%60
    minutes=math.floor(frames/(freq*60))
    return str(minutes)+':'+str(seconds)


class App(tkinter.Tk):
    def __init__(self, music_path, player, downloader):
        super().__init__()
        
        self.player = player
        self.downloader = downloader
        self.music_path = music_path

        self.title('music-bot')
        self.attributes('-fullscreen', True)

        self.initalize_app()


    def initalize_app(self):

        self.label = tkinter.Label(self, text = 'hello world')
        self.label.grid(row = 0, column = 0)

        self.close = tkinter.Button(self, text = 'close', command = self.destroy)
        self.close.grid(row = 0, column = 3)

        songs = sorted(os.listdir(self.music_path))

        self.song_list = tkinter.Listbox(self, height = 10, width = 20)
        for i in songs:
            self.song_list.insert(tkinter.ACTIVE, i)
        self.song_list.grid(row = 1, column = 0, rowspan= 3)

        self.play_btn = tkinter.Button(self, text = 'play song', command = self.set_slider)
        self.play_btn.grid(row = 1, column = 1)

        self.DLbtn = tkinter.Button(self, text = 'download', command = self.download)
        self.DLbtn.grid(row = 2, column = 1)


    def set_slider(self):
        self.player.set(f'{self.music_path}/{self.song_list.get(self.song_list.curselection())}')
        self.slider = tkinter.Scale(self, from_ = 0, to = self.player.song_length, orient = tkinter.HORIZONTAL, length = 200,command = self.change_slider, showvalue = 0)
        self.slider.grid(row = 4, column = 0, columnspan = 3)
        self.time_dis = tkinter.Label(self, text = '0:00')
        self.time_dis.grid(row = 5, column = 0)

    def change_slider(self, idk_what_this_is_supposed_to_be):
        self.player.change_time(self.slider.get())
        self.time_dis.config(text = convertMillis(self.slider.get(), self.player.freq))

    def update_slider(self, cur_time):
        pass

    def download(self):
        downloadwin = DownloadWindow(self, self.downloader)
        downloadwin.grab_set()


class DownloadWindow(tkinter.Toplevel):
    def __init__(self, master, downloader):
        super().__init__()
        self.master = master
        self.downloader = downloader
        self.geometry('1000x800')
        self.title('downloader')
        self.initialize_widgets()
    
    def initialize_widgets(self):
        self.textBox = tkinter.Entry(self, width = 100)
        self.textBox.grid(row=1, column = 0, columnspan = 2)

        self.searchBtn = tkinter.Button(self, text = 'search', command = lambda: self.search)
        self.searchBtn.grid(row = 2, column = 0)

        self.dlLinkBtn = tkinter.Button(self, text = 'download from link', width = 20)
        self.dlLinkBtn.grid(row = 2, column = 1)
        
        self.statusText = tkinter.Label(self, text = 'Enter name of a song in the box then click on \'search\' or enter a link then click on the \'download from link\' button')
        self.statusText.grid(row = 3, column = 0) 

        self.dlList = tkinter.Listbox(self, height= 100, width = 70)
        self.dlList.grid(row = 4, column = 0, rowspan=3, columnspan = 2)
        self.dlList.grid_forget()

        self.links = []

        self.dlBtn = tkinter.Button(self, text = 'download', command = lambda: self.downloader.download(self.links[self.dlList.curselection()[1]]))
        self.dlBtn.grid(row = 4, column = 2)
        self.dlBtn.grid_forget()
    
    def search(self):
        self.statusText.config(text = 'Searching, Please standby. Ignore the fact that program isnt responding')
        self.downloader.search(self.textBox.get())
        waiting = True
        while waiting:
            if self.downloader.status == 'idle':
                waiting = False
            else:
                time.wait(1)
        data = self.downloader.retrive
        for i in data:
            self.links.append(i['links'])
            insert = i['title'][:40] + ' ...' + i['duration']
            self.dlList.insert(tkinter.ACTIVE, insert)
        self.dlList.grid()
        self.dlBtn.grid()
        
        
        

        

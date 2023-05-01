from ui.main import App
from logic.playsound import Player
from logic.download import Downloader
import json


data = json.load(open('./data/data.json'))
music_path = data['music-path']

player = Player()
downloader = Downloader(music_path)

main_win = App(music_path, player, downloader)

main_win.mainloop()
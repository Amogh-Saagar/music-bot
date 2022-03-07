from __future__ import unicode_literals
import warnings
warnings.filterwarnings('ignore', '.*do not.*', )
warnings.warn('DelftStack')
warnings.warn('Do not show this message')
from googlesearch import search
import youtube_dl
import urllib
import shutil
import os
import threading
import multiprocessing
from bs4 import BeautifulSoup
import requests
from playsound import playsound
import random	
link = []
titles = []
download_input = False	
options = {
   	'format': 'bestaudio/best',
   	'postprocessors': [{
       	'key': 'FFmpegExtractAudio',
       	'preferredcodec': 'mp3',
       	'preferredquality': '128',
    		}],
}
print("""
	       Commands
	       	play [song name(exactly without character change)]
	       	download [song name to be searched]
	       	stop (to stop the song)
	       	stop dl (to stop download), not done yet
	""")
	
def dl(link, string):
	with youtube_dl.YoutubeDL(options) as ydl:
		info = ydl.extract_info(link, download=True)
		filename = ydl.prepare_filename(info)
	filename = filename.split('.')
	filename[len(filename)-1] = 'mp3'
	filename = '.'.join(filename)
	path = string+'.mp3'
	os.rename(filename, string+'.mp3')
	with open(path, 'rb') as f:
		file1 = open('songs/' + path, 'xb')
		file1. write(f.read())
		os.remove(path)
try:
	os.listdir('./songs')
except:
	
	os.makedirs('/home/amogh/Desktop/amogh sagar/coding/yt/songs' )
while True:
	input1 = input(']--')
	string = str(input1).lower().split()
	if string[0].lower() == 'play':
		song_name = ' '.join(string[1:])
		if song_name == 'n':
			text_files = [f for f in os.listdir('./songs') if f.endswith('.mp3')]
			song_name = './songs/' + random.choice(text_files)
		else:
			song_name =  './songs/' +song_name + '.mp3'
		p = multiprocessing.Process(target=playsound, args=(song_name,))
		p.start()
	elif string[0].lower() == 'stop':
		try:
			p.terminate()
		except:
			pass
	elif string[0].lower() == 'download' or string[0].lower() == 'dl' :
		print('downloading')
		link = []
		for j in search(f"{string} site:youtube.com", num=10,stop=10):
			link.append(j)
		for i in link:
			url = i
			reqs = requests.get(url)
			soup = BeautifulSoup(reqs.text, 'html.parser')
			for t in soup.find_all('title'):
				titles.append(t.get_text())
			#code from geekforgeeks
		download_name = ' '.join(string[1:])
		for n, i in enumerate(link):
			print(f'{n+1}: {titles[n]}')
			print()
		print('enter the number near the title which you want')
		download_input = True
	elif download_input:
		try:
			input_int = int(input1)
			download_thread = multiprocessing.Process(target=dl, args=(link[input_int-1], download_name,))
			download_thread.start()
		except:
			print('Please pass in a number')
'''			
	for j in search(f"{string} site:youtube.com", num=10,stop=20):
		link.append(j)
	json = simplejson.load(urllib.urlopen(url))
print(filename)
filename = filename.split('.')
filename[len(filename)-1] = 'mp3'
filename = '.'.join(filename)
os.rename(filename, string+'.mp3')
song = string+'.mp3'
t = threading.Thread(target=run, args=(song,))
t.start()
print(ok)
'''

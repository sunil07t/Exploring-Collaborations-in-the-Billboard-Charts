# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 15:34:53 2018

@author: Dane M4
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import pickle

def makeUrl():
    return "http://www.umdmusic.com/default.asp?Lang=English&Chart=D&ChDay=1&ChMonth=3&ChYear=2018&ChBand=&ChSong="


take = requests.get('http://www.umdmusic.com/default.asp?Lang=English&Chart=D&ChDay=10&ChMonth=3&ChYear=2018&ChBand=&ChSong=')
soup = BeautifulSoup(take.content, 'html.parser')
table = soup.find_all('td')

i = 9
start = 42

entries = []
songs = []
artist = []
date = []
enter = []
peak = []
weeks = []

while start < len(table):
    entries.append(str(table[start].text).strip())
    date.append(str(table[start+1].text).strip())
    enter.append(str(table[start+2].text).strip())
    peak.append(str(table[start+3].text).strip())
    weeks.append(str(table[start+4].text).strip())
    start += i

for entry in entries:
    split = entry.split('    ')
    songs.append(split[0])
    artist.append(split[-1].strip())

data = {'Arists':artist, 'Song':songs, 'Date':date, 'Entry':enter, 'Peak':peak, 'Weeks': weeks}

# Store through pickle
pickle.dump(data, open("top_chart_songs_data.p", "wb"))

# Test if save worked
data = {}
data = pickle.load(open("top_chart_songs_data.p", "rb"))

df = pd.DataFrame(data)

print df


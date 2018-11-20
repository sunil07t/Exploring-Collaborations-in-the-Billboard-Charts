# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 15:34:53 2018

@author: Dane M4
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def makeUrl(month, year):
    return "http://www.umdmusic.com/default.asp?Lang=English&Chart=D&ChDay=1&ChMonth="+str(month)+"&ChYear="+str(year)+"&ChBand=&ChSong="

month_start = 1
month_end = 12

start_year = 2009
end_year = 2017

songs = []
artist = []
date = []
enter = []
peak = []
weeks = []

def addMonth(month, year):
    entries = []
    start = 42
    i = 9
    take = requests.get(makeUrl(month, year))
    print('Accessing: ' + makeUrl(month, year))
    soup = BeautifulSoup(take.content, 'html.parser')
    table = soup.find_all('td')
    
    
    
    while start < len(table):
        entries.append((table[start].text).encode('utf-8').strip())
        date.append(str(table[start+1].text).strip())
        enter.append(str(table[start+2].text).strip())
        peak.append(str(table[start+3].text).strip())
        weeks.append(str(table[start+4].text).strip())
        start += i
    
    for entry in entries:
        split = entry.split('    ')
        songs.append(split[0])
        artist.append(split[-1].strip())

def makeDf():
    d = {'Arists':artist, 'Song':songs, 'Date':date, 'Entry':enter, 'Peak':peak, 'Weeks': weeks}

    return pd.DataFrame(d)

#while start_year <= end_year:
#    month_start = 1  
#    while month_start <= month_end:
#        addMonth(month_start, start_year)
#        month_start += 1
#    start_year += 1

#df = makeDf()

#df.to_csv('Billboard_top_09-17.csv')
        

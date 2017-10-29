# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:11:03 2017

@author: PeaceDove
"""

# monitor.py

import urllib
from xml.etree.cElementTree import parse

candidates = ['1866', '1383', '4367']
daves_lat =41.980262 

def distance(lat1, lat2):
    'Return distance in miles between two lats'
    return 69 * abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, daves_lat)
            print busid, dis, ' Miles' 
    print '--'*10
            
import time
while True:
    monitor()
    time.sleep(60)
    
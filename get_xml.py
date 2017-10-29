# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 19:06:27 2017

@author: PeaceDove
"""
import urllib
# import urllib.request # py3
u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
#u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22') # py3
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close

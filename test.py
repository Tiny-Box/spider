#-*- coding:utf-8
import BeautifulSoup 
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import os
import re

url = 'http://www.douban.com/group/topic/37742019/'

pageSource = requests.get(url)

page = []
page = urllib2.urlopen(url)
#page.split(',')
#print page


soup = BeautifulSoup(page)
barname = []
barname = soup.html.title.string
barname = re.sub(r'(\t|\s|\n|\r\n)', '', title)
 
print title

urllist = re.findall('\<a href\=\"(/.*)" title', page)

hrefs = []
results = soup.findAll('a', href = True)
for a in results:
	href = a.get('href').encode('utf-8')
	hrefs.append(href)


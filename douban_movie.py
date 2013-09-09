#!usr/bin/python
#coding:utf-8
'''
@author：Byron
新浪围脖：http://weibo.com/ziyuetk
'''
import urllib2
from bs4 import BeautifulSoup
print "豆瓣正在热映："
url = "http://movie.douban.com"
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html)
div_hot = soup.find('div',{"id":"screening"})
for i in div_hot.find_all('li', class_='title'):
    movie_title = i.a.get_text()
#   movie_title = movie_title.strip() #去除movie_title两边的空格
    print movie_title
 
print "\n豆瓣近期热门："
div_new = soup.find('div',{"id":"new-movies"})
for i in div_new.find_all('li', class_='title'):
    movie_new = i.a.get_text()
    print movie_new


#-*- coding:utf-8
import BeautifulSoup 
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://tieba.baidu.com/f?kw=2011superfive&fr=index&ie=utf-8'

pageSource = requests.get(url)

page = []
page = pageSource.text
page.split(',')
#print page

doc = ['<html><head><title>PythonClub.org</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b> of ptyhonclub.org.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b> of pythonclub.org.',
       '</html>']
soup = BeautifulSoup(''.join(page))
print soup.html.head.title
hrefs = []
results = soup.findAll('a', href = True)
for a in results:
	href = a.get('href').encode('utf-8')
	hrefs.append(href)

print hrefs

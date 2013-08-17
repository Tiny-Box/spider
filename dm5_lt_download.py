
import re
import urllib

def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

def getimg(html):
    #reg=r'class="zoom" file="\w.*.jpg"'
    #imgre=re.compile(reg)
    imglist=re.findall(r'http\:\/\/img142.*.jpg',html)
    print imglist
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%x)
        print x
        x+=1

address = raw_input("Pless input the URL")
print "plese wait...."


html=getHtml(address)
getimg(html)

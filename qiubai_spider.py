# -*- coding: utf8 -*-
import urllib2
import urllib
import re
import thread
import time

class HTML_Tool:
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
    
    EndCharToNoneRex = re.compile("<.*?>")

    BgnPartRex = re.compile("<p.*?>")
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")
    CharToNextTabRex = re.compile("<td>")

    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]
    
    def Replace_Char(self,x):
        x = self.BgnCharToNoneRex.sub("",x)
        x = self.BgnPartRex.sub("\n    ",x)
        x = self.CharToNewLineRex.sub("\n",x)
        x = self.CharToNextTabRex.sub("\t",x)
        x = self.EndCharToNoneRex.sub("",x)

        for t in self.replaceTab:
            x = x.replace(t[0],t[1])
        return x


class HTML_Model:
    
    def __init__(self):
        self.page = 1
        self.pages = []
        self.myTool = HTML_Tool()
        self.enable = False

    def GetPage(self,page):
        myUrl = "http://m.qiushibaike.com/hot/page/" + page
        myResponse  = urllib2.urlopen(myUrl)
        myPage = myResponse.read()
        unicodePage = myPage.decode("utf-8")

        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        return items

    def LoadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print '无法链接糗事百科！'
            else:
                time.sleep(1)
        
    def ShowPage(self,q,page):
        for items in q:
            print u'第%d页' % page , items[0]
            print self.myTool.Replace_Char(items[1])
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break
        
    def Start(self):
        self.enable = True
        page = self.page

        print u'正在加载中请稍候......'
        
        thread.start_new_thread(self.LoadPage,())
        
        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1


print u"""
---------------------------------------
   程序：糗百爬虫
   版本：0.1
   作者：why
   日期：2013-05-15
   语言：Python 2.7
   操作：输入quit退出阅读糗事百科
   功能：按下回车依次浏览今日的糗百热点
---------------------------------------
"""


print u'请按下回车浏览今日的糗百内容：'
raw_input(' ')
myModel = HTML_Model()
myModel.Start()

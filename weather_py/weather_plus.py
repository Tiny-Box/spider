#-*- coding:utf-8 -*-
import urllib2
import json

city = ["101020100", "101020500", "101021000"]

def weather():
	for citynum in city:
		try:
			url = 'http://m.weather.com.cn/data/%s.html' %citynum
			content = urllib2.urlopen(url).read()
			data = json.loads(content)
			result = data['weatherinfo']
			print result['city']
			for i in range(1, 7):
				print '%s\t%s' %(result['weather%s' %i], result['temp%s' %i])
			print '\t'
		except:
			print('查询失败')

weather()

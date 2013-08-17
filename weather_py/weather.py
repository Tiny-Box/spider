#!/usr/bin/env python2.7
#-*- coding:cp936 -*-
import urllib2
import json
from city import city

def weather():
	exit = False
	while not exit:
		cityname = raw_input("which city\'s weather do you want to get?\n")
		if cityname != 'n':
			citycode = city.get(cityname)
			if citycode:
				try:
					url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%citycode
					content = urllib2.urlopen(url).read()
					data = json.loads(content)
					result = data['weatherinfo']
					str_temp = ('%s\n%s ~ %s') %(
							result['weather'],
							result['temp1'],
							result['temp2']
							)
					print (str_temp)
				except:
					print('查询失败')
			else:
				print('没有找到该城市')
		else:
			exit = True

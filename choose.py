# -*- coding:utf-8
import urllib
import urllib2 as ur
# import http.cookiejar as hc
import cookielib

ua = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.66 Safari/537.36'

cj = cookielib.CookieJar()

cookie_support = ur.HTTPCookieProcessor(cj)
opener = ur.build_opener(cookie_support)
ur.install_opener(opener)

username = '123456'
password = '123456'
postdata = {'Login.Token1':username, 'Login.Token2':password}

login_url = 'http://tjis2.tongji.edu.cn:58080/amserver/UI/Login'
enter_url = 'http://4m3.tongji.edu.cn/eams/tJStdElectCourse!defaultPage.action?electionProfile.id=1985'
class_url = 'http://4m3.tongji.edu.cn/eams/tJStdElectCourse!batchOperator.action?electLessonIds=111111111823226%2C&withdrawLessonIds=&exchangeLessonPairs=&_=1420557098832'

# url = login_url + '&'
Data = ''
for (k,v) in  postdata.items():
        Data += '&' + k + '=' + v

res = ur.urlopen(login_url, data=Data)
# print res.read()

res = ur.urlopen(enter_url, data=Data)
# info = ur.urlopen(enter_url, data=Data).info()
# print res.read().decode(info.getparam('charset')).encode('gbk')

cnt = 0

while (1):
	res = ur.urlopen(class_url)
	tmp = res.read().decode('utf-8')
	print tmp
	str = "elected : true"
	pos = tmp.find(str.decode('utf-8'))
	if (pos == -1):
		break;
	cnt += 1
	print "失败, ", cnt

print "成功, ", cnt
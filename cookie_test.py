# -*- coding: utf-8 -*-
'''import cookielib
import urllib2

cookie = cookielib.CookieJar()

cookie_Hp = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(cookie_Hp)

response = opener.open("http://www.renren.com")

for i in cookie :
	print "name", i.name
	print "value", i.value
'''


                
import urllib2, urllib, cookielib, re
                
class LoginRenren(object):
                
    """登陆人人构造器"""
                
    def __init__(self, email, password):
                
        self.email = email
        self.password = password
        self.domain = 'renren.com'
        self.logined_url = ''
        self.logined_url_re = r'http://www.renren.com/\d{9}'
        self.islogin = False
                
        try:
            # 获取构建cookie
            cookie = cookielib.CookieJar()
            cookieProc = urllib2.HTTPCookieProcessor(cookie)
        except:
            raise
        else:
            #装载cookies    
            opener = urllib2.build_opener(cookieProc)
            urllib2.install_opener(opener)
                
    def login(self):
                        
        """登陆方法"""
                
        print 'login...'
        # 登陆地址
        url='http://www.renren.com/PLogin.do'
        # post数据
        postdata = {
            'email': self.email,
            'password': self.password,
            'domain': self.domain
        }
        # 编码登陆的post数据
        data = urllib.urlencode(postdata)
        # 构造请求
        req = urllib2.Request(
            url,
            data
        )
        # 发送请求，获取响应
        # response = opener.open(req) 
        response = urllib2.urlopen(req) 
        # 登陆后的url
        self.logined_url = response.geturl()
                
                
        # 判断登陆是否成功
        self.__isLogin()
        if self.islogin == True:
            print u'登陆成功 !'
            self.__getStatus()
        else:
            print u'登录失败，请重试 !'
                
                
    def __isLogin(self):
                
        """判断登陆是否成功"""
                
        if re.search(self.logined_url_re, self.logined_url) != None:
            self.islogin = True
                
    def __getStatus(self):
        pass

	def friends_get(self):
		myPage = urllib2.urlopen(self.url).read().decode("gbk")
		print myPage
                
if __name__ == '__main__':
                    
    # 请输入您的用户名
    EMAIL = raw_input(u'email:')
    # 请输入您的密码
    PASSWORD = raw_input(u'password:')
                        
    lr = LoginRenren(EMAIL, PASSWORD)
    lr.login()
    lr.friends_get()

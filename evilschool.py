import urllib
import urllib2 as ur
from lxml import etree

def get_context(url):
	opener = ur.build_opener()
	opener.addheaders.append(('Host', "tw.seemh.com"))
	opener.addheaders.append(('User-Agent', "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0"))
	opener.addheaders.append(('Accept', "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"))
	opener.addheaders.append(('Accept-Language', "zh-CN,en-US;q=0.7,en;q=0.3"))
	opener.addheaders.append(('Accept-Encoding', "gzip, deflate"))
	opener.addheaders.append(('Connection', "keep-alive"))
	opener.addheaders.append(('If-Modified-Since', "Thu, 21 May 2015 08:43:21 GMT"))
	opener.addheaders.append(('Cache-Control', "max-age=0"))
	opener.addheaders.append(('Cookie', 'behe_cookiesmapping=1; Hm_lvt_38a1bab61660f620209480de377747ed=1432799230; Hm_lpvt_38a1bab61660f620209480de377747ed=1432825208; lzstat_uv=6529783541600131720|3554287; lzstat_ss=292155713_1_1432853697_3554287; a8284_pages=2; a8284_times=1'))
	ur.install_opener(opener)

	f = ur.urlopen(url)
	# print f.read().decode('utf-8').encode('GB18030')
	return f.read().lower().decode('utf-8')

def download(url):
	# page_list = {}
	html_element = etree.HTML(get_context(url))
	status_element_list = html_element.xpath(".//a[@class='status0']")

	for status_element in status_element_list:
		inner_html = etree.tostring(status_element)

		page_name_text = etree.HTML(inner_html).find(".//span").text
		page_name = filter(lambda ch: ch in '0123456789.', page_name_text)

		page_num_text = etree.HTML(inner_html).find(".//i").text
		page_num = filter(str.isdigit, page_num_text)

		download_file(page_name, page_num)
		

	# print page_list
	# return page_list

def download_file(name, page):
	url_part_one = "http://idx.seemh.com:88/ps1/h/HSdd/Act_"
	url_part_two = "/xindm_cn_"
	url_part_three = ".png"

	for item in range(page):
		img = ur.urlopen(url_part_one+name.replace('.', '_')+url_part_two+"{0:0>3d}{1:0>3d}".format(item-1, item)+url_part_three)
		with open('/name/{0}.jpg'.format(item),'wb') as imgfile:
			imgfile.write(img.read())


def main():
	url_test = "http://tw.seemh.com/comic/1152/"

	download(url_test)
	# context = get_context(url_test)
	# get_page_list(context)



if __name__ == '__main__':
	main()
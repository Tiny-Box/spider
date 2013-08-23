import BeautifulSoup 
import requests

url = 'http://tieba.baidu.com/f?kw=2011superfive&fr=index&ie=utf-8'

pageSource = requests.get(url)

hrefs = []
soup = BeautifulSoup(pageSource)
results = soup.find_all('a', href = True)
for a in results:
	href = a.get('href').encode('utf-8')
	if not href.startswith('http'):
		href = urljoin(url, href)
	hrefs.append(href)

print hrefs

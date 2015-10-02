#coding=utf-8
import requests
from operator import itemgetter

minelist = [
	[1230, '凡晶石', 0.1],
	[18, '斜长岩', 0.35],
	[19, '灰岩', 16],
	[20, '水硼砂', 1.2],
	[21, '同位原矿', 3],
	[22, '艾克诺岩', 16],
	[1223, '双多特石', 16],
	[1224, '干焦岩', 0.3],
	[1225, '克洛基石', 16],
	[1226, '杰斯贝矿', 2],
	[1228, '灼烧岩', 0.15],
	[1229, '片麻岩', 5],
	[1231, '希莫非特', 3],
	[1232, '黑赭石', 8],
	[11396, '基腹断岩', 40],
	[17425, '红色艾克诺岩', 16],
	[17428, '三晶双多特斜岩', 16],
	[17429, '单晶双多特斜岩', 16],
	[17432, '斜克洛基石', 16],
	[17433, '克洛基水晶', 16],
	[17437, '黑曜赭石', 8],
	[17440, '玻璃状同位原矿', 3],
	[17441, '光面同位原矿', 3],
	[17444, '多色希莫非特', 3],
	[17445, '辐射希莫非特', 3],
	[17448, '纯杰斯贝矿', 2],
	[17449, '朴质杰斯贝矿', 2],
	[17452, '发光水硼砂', 1.2],
	[17453, '灼热水硼砂', 1.2],
	[17455, '蓝色斜长岩', 0.35],
	[17456, '富斜长岩', 0.35],
	[17459, '固体干焦岩', 0.3],
	[17460, '流体干焦岩', 0.3],
	[17463, '浓缩灼烧岩', 0.15],
	[17464, '厚灼烧岩', 0.15],
	[17466, '亮灰岩', 16],
	[17467, '发光灰岩', 16],
	[17470, '富凡晶石', 0.1],
	[17471, '厚质凡晶石', 0.1],
]

normal_mine_list = [
	[1230, '凡晶石', 0.1],
	[18, '斜长岩', 0.35],
	[20, '水硼砂', 1.2],
	[1224, '干焦岩', 0.3],
	[1228, '灼烧岩', 0.15],
	[1229, '片麻岩', 5],
	[17452, '发光水硼砂', 1.2],
	[17453, '灼热水硼砂', 1.2],
	[17455, '蓝色斜长岩', 0.35],
	[17456, '富斜长岩', 0.35],
	[17459, '固体干焦岩', 0.3],
	[17460, '流体干焦岩', 0.3],
	[17463, '浓缩灼烧岩', 0.15],
	[17464, '厚灼烧岩', 0.15],
	[17470, '富凡晶石', 0.1],
	[17471, '厚质凡晶石', 0.1],
]

mine_item = []

for item in normal_mine_list:
	url = 'http://www.ceve-market.org/api/market/region/10000002/system/30000142/type/{0}.json'.format(str(item[0]))
	r = requests.get(url)
	res = r.json()
	buy = res['buy']['max'] / item[2] 

	item_price = {
		'name': item[1],
		'price': buy
	}
	mine_item.append(item_price)


mine_by_price = sorted(mine_item, key=itemgetter('price'), reverse=True)

print('=======================================')

for item in mine_by_price:
	print('{0}\t每立方出售:{1:.2f}  '.format(item['name'].ljust(8), item['price']))
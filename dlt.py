# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import json
# html = urlopen('http://tubiao.zhcw.com/tubiao/dlt/dltJsp/dlt_zongHeFenBuTuAsc.jsp?select=1')
# bs = BeautifulSoup(html.read(),'html.parser')

# table = bs.findAll('table',{'class':'tab_dlt'})

# # print(table)

# for tr in table:
# 	t = tr.find_all('tr')
# 	print(t)
# 	# break
# # for red in table:
# # 	redball = red.find_all('td',{'class':{'bgcolor_zh10'}})
# # 	print(redball)
# # 	break

# # for name in namelist:
# # 	t = name.find_all('',{'class':{'qh7','redqiu','blueqiu3'}})
# # 	# print(t)
# # 	i = 0
# # 	for a in t:
# # 		if a.find('a') != None:
# # 			print(i,a.find('a'))
# # 		if i > 0:
# # 			print(i,a.get_text())
# # 		i=i+1
# # 	# break

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from itertools import combinations
from collections import Counter
html = urlopen('http://tubiao.zhcw.com/tubiao/dlt/dltJsp/dlt_zongHeFenBuTuAsc.jsp?select=300')
bs = BeautifulSoup(html.read(),'html.parser')
namelist = bs.findAll('tr',{'class':''}) 
redline = []
for balls in namelist:
	opendate = balls.find_all('td',{'class':'kjhm_1'})
	redall = []
	for o in opendate:
		# redall.append(o[0:2])
		# redall.append(o[3:5])
		# redall.append(o[6:8])
		# redall.append(o[9:11])
		# redall.append(o[12:14])
		s=o.get_text()
		redall.append(s[1:3])
		redall.append(s[5:7])
		redall.append(s[9:11])
		redall.append(s[13:15])
		redall.append(s[17:19])
		# print(s[5:7])
	redline.append(redall)
print(redline)
		# print(o.get_text())
	# for o in opendate:
	# 	# print(o)
	# red = balls.find_all('td',{'class':'redqiu'})
	# # print("red ball are:")
	# redstr =[]
	# for r in red:
	# 	redstr.append(r.get_text())
	# redlist = list(combinations(redstr,2))
	# redall = redall + redlist
	# # Counter(redall)
	# # print(redall)

	# # print("blue ball is:")
	# blue = balls.find_all('td',{'class':'blueqiu3'})
	# # for b in blue:
	# 	# print(b.get_text())
	# print("---")

# x=Counter(redall)
# print(x)




# for name in namelist:
# 	t = name.find_all('',{'class':{'qh7','redqiu','blueqiu3'}})
# 	# print(t)
# 	i = 0
# 	for a in t:
# 		if a.find('a') != None:
# 			print(i,a.find('a'))
# 		if i > 0:
# 			print(i,a.get_text())
# 		i=i+1
# 	# break
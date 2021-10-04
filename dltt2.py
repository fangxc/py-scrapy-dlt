from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
from itertools import combinations
from collections import Counter
import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# urlStr='https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&isVerify=1&termLimits=1'

# html = urlopen(urlStr)
# bs = BeautifulSoup(html.read(),'html.parser')
# print(bs)


# data = {
#     "country": "Germany",
#     "vehicle": {
#         "name": "Volkswagen",
#         "model": "T-Roc"
#     }
# }

data = {
"dataFrom":"",
"emptyFlag":"false",
"errorCode":"0",
"errorMessage":"处理成功",
"success":"true",
"value":{
	"list":[
		{
			"drawFlowFund":"0",
			"drawFlowFundRj":"",
			"estimateDrawTime":"",
			"isGetKjpdf":1,
			"isGetXlpdf":2,
			"lotteryDrawNum":"21102",
			"lotteryDrawResult":"02 08 11 16 23 02 07",
			"lotteryDrawStatus":20,
			"lotteryDrawTime":"2021-09-04",
			"lotteryEquipmentCount":1,
			"lotteryGameName":"超级大乐透",
			"lotteryGameNum":"85",
			"lotteryGamePronum":0,
			"lotteryPaidBeginTime":"2021-09-04 22:00:01",
			"lotteryPaidEndTime":"2021-11-03 23:59:59",
			"lotteryPromotionFlag":1,
			"lotterySaleBeginTime":"2021-09-01 20:10:00",
			"lotterySaleEndTimeUnix":0,
			"lotterySaleEndtime":"2021-09-04 20:00:00",
			"lotterySuspendedFlag":0,
			"lotteryUnsortDrawresult":"16+02+11+08+23 02+07",
			"matchList":[],"pdfType":1,
			"poolBalanceAfterdraw":"982,320,278.84",
			"poolBalanceAfterdrawRj":"",
			"prizeLevelList":[
				{"awardType":0,"group":"101","lotteryCondition":"","prizeLevel":"一等奖","sort":101,"stakeAmount":"7,523,067","stakeCount":"13","totalPrizeamount":"97,799,871"},
				{"awardType":0,"group":"201","lotteryCondition":"","prizeLevel":"一等奖(追加)","sort":201,"stakeAmount":"6,018,453","stakeCount":"5","totalPrizeamount":"30,092,265"},
				{"awardType":0,"group":"301","lotteryCondition":"","prizeLevel":"二等奖","sort":301,"stakeAmount":"111,145","stakeCount":"117","totalPrizeamount":"13,003,965"},
				{"awardType":0,"group":"401","lotteryCondition":"","prizeLevel":"二等奖(追加)","sort":401,"stakeAmount":"88,916","stakeCount":"66","totalPrizeamount":"5,868,456"},
				{"awardType":0,"group":"501","lotteryCondition":"","prizeLevel":"三等奖","sort":501,"stakeAmount":"10,000","stakeCount":"253","totalPrizeamount":"2,530,000"},
				{"awardType":0,"group":"601","lotteryCondition":"","prizeLevel":"四等奖","sort":601,"stakeAmount":"3,000","stakeCount":"896","totalPrizeamount":"2,688,000"},
				{"awardType":0,"group":"701","lotteryCondition":"","prizeLevel":"五等奖","sort":701,"stakeAmount":"300","stakeCount":"17,767","totalPrizeamount":"5,330,100"},
				{"awardType":0,"group":"801","lotteryCondition":"","prizeLevel":"六等奖","sort":801,"stakeAmount":"200","stakeCount":"22,665","totalPrizeamount":"4,533,000"},
				{"awardType":0,"group":"901","lotteryCondition":"","prizeLevel":"七等奖","sort":901,"stakeAmount":"100","stakeCount":"41,183","totalPrizeamount":"4,118,300"},
				{"awardType":0,"group":"1001","lotteryCondition":"","prizeLevel":"八等奖","sort":1001,"stakeAmount":"15","stakeCount":"698,565","totalPrizeamount":"10,478,475"},
				{"awardType":0,"group":"1101","lotteryCondition":"","prizeLevel":"九等奖","sort":1101,"stakeAmount":"5","stakeCount":"6,882,807","totalPrizeamount":"34,414,035"}
			],
			"prizeLevelListRj":[],
			"ruleType":0,"termList":[],
			"totalSaleAmount":"305,869,819",
			"totalSaleAmountRj":"",
			"verify":1,"vtoolsConfig":{}
		}],
		"pageNo":1,
		"pageSize":1,
		"pages":1,"total":1
		}
}


print(json.dumps(data))

# balltable = bs.findAll('table',{'id':'table_dlt'})
# print(balltable)


# redString = 'bgcolor_zh2'
# blueString = 'bgcolor_zh10'

# nextRed1 = False
# nextRed2 = False
# nextRed3 = False
# nextRed4 = False
# nextRed5 = False

# nextBlue1 = False
# nextBlue1 = False
# blue1 = []
# blue1 = []

# red1 = []
# red2 = []
# red3 = []
# red4 = []
# red5 = []


# html = urlopen('https://tubiao.zhcw.com/tubiao/dlt/dltJsp/dlt_zongHeFenBuTuAsc.jsp?select=300')
# bs = BeautifulSoup(html.read(),'html.parser')
# namelist = bs.findAll('table',{'id':'table_dlt'})

# # print(bs)

# for balls in namelist:
# 	found=True
# 	# opendate = balls.find_all('td',{'class':'qh7'})
# 	# for o in opendate:
# 	# 	oss=o.get_text()
# 	# 	if(oss.find("模拟")==-1 and oss !=benqi):
# 	# 		# print(oss)
# 	# 		yy=1
# 	# 	else:
# 	# 		found=False;
# 	if found:
# 		red = balls.find_all('td',{'class':redString}) 
# 		blue = balls.find_all('td',{'class':blueString})
# 		redstr =[]
# 		bluestr = []
# 		for r in red:
# 			redstr.append(r.get_text())
# 		if nextRed1:
# 			red1.append(redstr[0])
# 			nextRed1 = False
# 		if nextRed2:
# 			red2.append(redstr[1])
# 			nextRed2 = False
# 		if nextRed3:
# 			red3.append(redstr[2])
# 			nextRed3 = False
# 		if nextRed4:
# 			red4.append(redstr[3])
# 			nextRed4 = False
# 		if nextRed5:
# 			red5.append(redstr[4])
# 			nextRed5 = False
# 		if nextRed6:
# 			red6.append(redstr[5])
# 			nextRed6 = False

# 		for b in blue:
# 			bluestr.append(b.get_text())
# 		if nextBlue1:
# 			blue1.append(bluestr[0])
# 			nextBlue1 = False

# 		if(currball[0]==redstr[0]): 
# 			nextRed1 = True;
# 		if(currball[1]==redstr[1]): 
# 			nextRed2 = True;
# 		if(currball[2]==redstr[2]): 
# 			nextRed3 = True;
# 		if(currball[3]==redstr[3]): 
# 			nextRed4 = True;
# 		if(currball[4]==redstr[4]): 
# 			nextRed5 = True;
# 		if(currball[5]==redstr[5]): 
# 			nextRed6 = True;

# 		if(currball[6]==bluestr[0]): 
# 			nextBlue1 = True;

# 		# if(currball[0]==redstr[0]): 
# 		# 	print("red1=",currball[0],redstr)
# 		# if(currball[1]==redstr[1]): print("red2=",currball[1],redstr)
# 		# if(currball[2]==redstr[2]): print("red3=",currball[2],redstr)
# 		# if(currball[3]==redstr[3]): print("red4=",currball[3],redstr)
# 		# if(currball[4]==redstr[4]): print("red5=",currball[4],redstr)
# 		# if(currball[5]==redstr[5]): print("red6=",currball[5],redstr)
# 		# else:
# 		# 	print("===",redstr)

# 		# print("blue ball is:")
# 		# blue = balls.find_all('td',{'class':'blueqiu3'})
# 		# for b in blue:
# 		# 	print(b.get_text())
# 		# print("---")

# print("red1: ", Counter(red1))
# print()
# print("red2: ",Counter(red2))
# print()
# print("red3: ",Counter(red3))
# print()
# print("red4: ",Counter(red4))
# print()
# print("red5: ",Counter(red5))
# print()
# print("red6: ",Counter(red6))

# print()
# print("blue: ",Counter(blue1))



# html = urlopen('https://tubiao.zhcw.com/tubiao/dlt/dltJsp/dlt_zongHeFenBuTuAsc.jsp?select=30')
# bs = BeautifulSoup(html.read(),'html.parser')

# balltable = bs.findAll('table',{'id':'table_dlt'})

# # print(balltable)

# reds = []
# blues = []

# nextRed1 = False
# nextRed2 = False
# nextRed3 = False
# nextRed4 = False
# nextRed5 = False

# red1 = []
# red2 = []
# red3 = []
# red4 = []
# red5 = []

# for lr in balltable:
# 	trtr = lr.find_all('tr')
# 	for tdd in trtr:
# 		rdd = tdd.find_all('td',{'class':'bgcolor_zh2'})
# 		for x in rdd:
# 			reds.append(x.get_text())
# 		if nextRed1:
# 			red1.append(redstr[0])
# 			nextRed1 = False
# 		if nextRed2:
# 			red2.append(redstr[1])
# 			nextRed2 = False
# 		if nextRed3:
# 			red3.append(redstr[2])
# 			nextRed3 = False
# 		if nextRed4:
# 			red4.append(redstr[3])
# 			nextRed4 = False
# 		if nextRed5:
# 			red5.append(redstr[4])
# 			nextRed5 = False
# 		if(currball[0]==redstr[0]): 
# 			nextRed1 = True;
# 		if(currball[1]==redstr[1]): 
# 			nextRed2 = True;
# 		if(currball[2]==redstr[2]): 
# 			nextRed3 = True;
# 		if(currball[3]==redstr[3]): 
# 			nextRed4 = True;
# 		if(currball[4]==redstr[4]): 
# 			nextRed5 = True;



# 			# print(x.get_text())
# 		bld = tdd.find_all('td',{'class':'bgcolor_zh10'})
# 		for y in bld:
# 			blues.append(y.get_text())

# print(reds)
# print(blues)


# print(namelist)
# currball = []
# benqi = ""
# for balls in namelist:
# 	opendate = balls.find_all('td',{'class':'kjhm_3'},{'class':'kjhm_1'})
# 	print(opendate)
# 	for o in opendate:
# 		oss=o.get_text()
# 		if(oss.find("模拟")==-1):
# 			benqi=oss
# 			print(benqi)

# 	red = balls.find_all('td',{'class':'redqiu'}) 
# 	for r in red:
# 		currball.append(r.get_text())

# 	# print("blue ball is:")
# 	# blue = balls.find_all('td',{'class':'blueqiu3'})
# 	# for b in blue:
# 	# 	print(b.get_text())
# 	# print("+++++++++++++++++++++")
# print(currball)
# print()



# html = urlopen('http://tubiao.zhcw.com/tubiao/ssqNew/ssqJsp/ssqZongHeFengBuTuAsc.jsp?select=200')
# bs = BeautifulSoup(html.read(),'html.parser')
# namelist = bs.findAll('tr',{'class':'hgt'})
# for balls in namelist:
# 	found=True
# 	opendate = balls.find_all('td',{'class':'qh7'})
# 	for o in opendate:
# 		oss=o.get_text()
# 		if(oss.find("模拟")==-1 and oss !=benqi):
# 			print(oss)
# 		else:
# 			found=False;
# 	if found:			
# 		red = balls.find_all('td',{'class':'redqiu'}) 
# 		redstr =[]
# 		for r in red:
# 			redstr.append(r.get_text())
# 		if(currball[5]==redstr[5]): 
# 			print("red6=",currball[5],redstr)
# 		# if(currball[1]==redstr[1]): print("red2=",currball[1],redstr)
# 		# if(currball[2]==redstr[2]): print("red3=",currball[2],redstr)
# 		# if(currball[3]==redstr[3]): print("red4=",currball[3],redstr)
# 		# if(currball[4]==redstr[4]): print("red5=",currball[4],redstr)
# 		# if(currball[5]==redstr[5]): print("red6=",currball[5],redstr)
# 		else:
# 			print("===",redstr)

# 		# print("blue ball is:")
# 		# blue = balls.find_all('td',{'class':'blueqiu3'})
# 		# for b in blue:
# 		# 	print(b.get_text())
# 		# print("---")
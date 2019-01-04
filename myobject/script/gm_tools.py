#-*- coding:utf-8 -*-

import requests
import json
from multiprocessing import Pool
import time


class Gmtools(object):
	def __init__(self):
		self.ip = "http://109.244.1.51:50280/gd?"
		self._ip = "http://109.244.1.50:50180/gd?"
		self._800_ip = "http://139.199.165.219:50080/gd?"
		self.param1 = "gs"
		self.card_list = ['6001',
							'6002',
							'6003',
							'6004',
							'6005',
							'6006',
							'6007',
							'6008',
							'6009',
							'6010',
							'6011',
							'6012',
							'6013',
							'6014',
							'6015',
							'6016',
							'6017',
							'6018',
							'6019',
							'6020',
							'6021',
							'6022',
							'6023',
							'6024',
							'6025',
							'6026',
							'6027',
							'6028',
							'6029',
							'6030',
							'6031',
							'6032',
							'6033',
							'6034',
							'6035',
							'6036',
							'6037',
							'6038',
							'6039',
							'6040',
							'6041',
							'6042',
							'6043',
							'6044',
							'6045',
							'6048',
							'6049',
							'6050',
							'6051',
							'6052',
							'6055',
							'6047',
							'6057',
							'6058',
							'6059',
							'6072',
							'6083',
							'6084',
							'6067',
							'6068']

		self.add_produce_count = {
							    1200 : 10000,
							    1201 : 10000,
							    1202 : 10000,
							    1203 : 10000,
							    1204 : 10000,
							    1205 : 10000,
							    1206 : 10000,
							    1207 : 10000,
							    1208 : 10000,
							    1209 : 10000,
							    1210 : 10000,
							    1211 : 10000,
							    1212 : 10000,
							    1213 : 10000,
							    1214 : 10000,
							    1215 : 10000,
							    1216 : 10000,
							    1217 : 10000,
							    1218 : 10000,
							    1219 : 10000,
							    1220 : 10000,
							    1221 : 10000,
							    1222 : 10000,
							    1223 : 10000,
							    1224 : 10000,
							    1225 : 10000,
							    1226 : 10000,
							    1227 : 10000,
							    1228 : 10000,
							    1229 : 10000,
							    1230 : 10000,
							    1231 : 10000,
							    1232 : 10000,
							    1233 : 10000,
							    1234 : 10000,
							    1235 : 10000,
							    1236 : 10000,
							    1237 : 10000,
							    1004 : 10000,
							    7001 : 10000,
							    1237 : 10000,
							    1238 : 10000,
							    4008 : 5000,
							    1800 : 10000,
							    1801 : 10000,
							    1802 : 10000,
							    1803 : 10000,
							    1804 : 10000,
							    1600 : 10000,
							    1601 : 10000,
							    1602 : 10000,
							    1603 : 10000,
							    1604 : 10000,
							    1605 : 10000
								}
		self.help_task_list = [
					6001,
					6002,
					6003,
					6004,
					6005,
					6006,
					6007,
					6008,
					6009,
					6010,
					6011,
					6012,
					6013,
					6014,
					6015,
					6016,
					6017,
					6018,
					6019,
					6020,
					6021,
					6022,
					6023,
					6024,
					6025
		]

	def order(self,roleid,func,__id,server,count=None,):
		api = ''
		dic1 =[
			{'mod':'0'},
			{'id':'0'},
			{'comm':func},

		]
		# dic2 = [
		# 		{roleid:roleid},
		# 		{_id:_id},
		# 		{count:count}
		# 		]
		dic2 = {'roleid':roleid,'_id':__id,'count':count}
		sign = '%7C'
		for x in dic1:
			for k,v in x.items():
				if k != 'comm':
					api = api + k + "=" + v + "&"
				elif k == 'comm':
					api = api + k + "=" + v
		if count != None:
			api = api + sign + dic2['roleid'] + sign + dic2['_id'] + sign + dic2['count']
		else:
			api = api + sign + dic2['roleid'] + sign + dic2['_id']
		_ip = {'server_1':self._ip,'server_2':self.ip,'server_800':self._800_ip}
		# if ip != None:
		# 	api = self._ip + api
		# else:
		# 	api = self.ip + api
		api = _ip[server] + api
		api.decode('utf-8')
		print '---------------------------'
		print api
		response = requests.get(api)
		print response.text

	def set_team_level(self,roleid,num,server):
		self.order(roleid,'set_team_level',num,server)
		return 

	def add_hero(self,roleid,server):
		hero_list = self.card_list
		for x in hero_list:
			self.order(roleid,'create_item',x,server,'1999')
		return
	
	def add_startstone(self,roleid,server):
		star_stone = ['50004','50005']
		for x in star_stone:
			self.order(roleid,'create_item',x,server,'500')
		return 

	def set_money(self,roleid,money_type,num,server):
		self.order(roleid,'set_money',money_type,server,num)
		return

	def clear_help_task(self,roleid,server):
		for x in self.help_task_list:
			self.order(roleid,'task_passed',str(x),server,'2')
			# p = Pool()
			# p.apply_async(self.order,args=(roleid,'task_passed',str(x),server,'2'))
		return

	def set_dup_process(self,roleid,server,dupid):
		self.order(roleid,'set_dup_progress',dupid,server)
		return 


	def create_all_item(self,roleid,server):
		item_dic = self.add_produce_count
		self.set_team_level(roleid,'70',server)
		self.add_hero(roleid,server)
		self.add_startstone(roleid,server)
		self.set_money(roleid,'1','999999999',server)
		self.set_money(roleid,'2','999999999',server)
		for prod in item_dic:
			self.order(roleid,'create_item',str(prod),server,str(item_dic[prod]))
		return


	def super_man(self,roleid,server,userlevel):
		item_dic = self.add_produce_count
		self.set_team_level(roleid,userlevel,server)
		self.add_hero(roleid,server)
		self.add_startstone(roleid,server)
		self.set_money(roleid,'1','999999999',server)
		self.set_money(roleid,'2','999999999',server)
		self.set_dup_process(roleid,server,'10640') #临时修改
		self.clear_help_task(roleid,server)
		for prod in item_dic:
			self.order(roleid,'create_item',str(prod),server,str(item_dic[prod]))
		return


	def clear_dup_task(self,roleid,server,duptask=range(1002001,1002049),switch='2'):
		dup_task = duptask
		for x in dup_task:
			self.order(roleid,'task_passed',str(x),server,switch)
			time.sleep(3)
		return

	def set_quest_activity(self,roleid,server,duptask,switch='2'):
		dup_task = duptask
		for x in dup_task:
			self.order(roleid,'set_quest_activity',str(x),server,switch)
		return 
if __name__ == '__main__':
	tar = Gmtools()
	#tar.create_all_item('8000000036','server_800')
	#tar.super_man('9940042518','server_1','56')
	#tar.clear_help_task('9940042560','server_1')
	#tar.clear_dup_task('9940051419','server_1')
	tar.set_quest_activity('9940000027','server_1',[5101,
5102,
5103,
5104,
5105,
5106,
5107,
5108,
5109,
5110,
5111,
5201,
5202,
5203,
5204,
5205,
5206,
5207,
5208,
5209,
5210,
5211,
5212,
5301,
5302,
5303,
5304,
5305,
5306,
5307,
5308,
5309,
5310,
5401,
5402,
5403,
5404,
5405,
5406,
5407,
5408,
5409,
5410,
5501,
5502,
5503,
5504,
5505,
5506,
5507,
5508,
5509,
5510,
5601,
5602,
5603,
5604,
5605,
5606,
5607,
5608,
5609,
5610,
5701,
5702,
5703,
5704,
5705,
5706,
5707,
5708,
5709,
5710,
5711],'3')
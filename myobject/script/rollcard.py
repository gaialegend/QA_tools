#-*- coding:utf-8 -*-

import csv2name
import gm_tools
import requests
import json

class rollcard(gm_tools.Gmtools):
	def __init__(self):
		gm_tools.Gmtools.__init__(self)

	def rollcard_post(self,role_id,count,_type,pool,server):
		#钻石单抽 0
		#抽奖券抽 1
		#十连抽 2
		api = ''
		# dic1 =[
		# 	{'mod':'0'},
		# 	{'id':'0'},
		# 	{'comm':'rollcard'},
		# 	{'rollcard_id':'0'}
		# 	{'rollcard_type':'0'}
		# 	]
		sign = '%7C'
		_ip = {'server_1':self._ip,'server_2':self.ip}
		api = _ip[server] + 'mod=0&id=0&comm=rollcard'+sign+role_id+sign+str(pool)+sign+str(_type)+sign+count
		print api
		response = requests.get(api)
		res = response.json()
		print res
		res = res['msg']
		print '----------------------------------------'
		print res
		dic_res = eval(res)
		#print type(dic_res)
		if str(_type) == '2':
			count = int(count) * 10
		filename = csv2name.report(dic_res,count)
		return filename
		

if __name__ == '__main__':
	tar = rollcard()
	tar.set_money('9940042526','2','999999999','server_1')
	tar.order('9940042526','create_item','1012','server_1','10000')
	tar.rollcard_post('9940042526','10000',0,2)
	tar.rollcard_post('9940042526','10000',1,2)
	tar.rollcard_post('9940042526','1000',2,2)
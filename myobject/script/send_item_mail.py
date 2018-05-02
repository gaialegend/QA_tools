#-*- coding:utf-8 -*-

import requests
from csv2name import get_item_id

ip = "http://115.182.192.230:50180/gd?"

def send_req(func_name,role_id,*params):
	global ip
	sign = '%7C'
	sign2 = '%2C'
	context = ip+'mod=0&id=0&comm='+func_name + sign+role_id+sign
	for x in params:
		#print type(x)
		if type(x) == list:
			#lastpos = len(x) -1
			context_2 = ''
			for index in range(len(x)):
				if index != (len(x) - 1):
					context_2 = context_2 + str(x[index]) +sign2
				else:
					context_2 = context_2 + str(x[index])
			context = context + context_2 + sign
		else:
			context = context + str(x) + sign
	print context
	response = requests.get(context)
	#print context
	#print response.text
	return 





def send_item_mail(role_id):
	item_dic = get_item_id()
	times = 0
	for key in item_dic:
		li = [item_dic[key],key,1]
		times += 1
		try:
			send_req('send_item_mail',role_id,'item_test','item','test',li,0,0)
		except:
			print times


if __name__ == '__main__':
	#send_req('send_item_mail','9940042526','item_test','item','test',[1,1,1],0,0)
	send_item_mail('9940042526')

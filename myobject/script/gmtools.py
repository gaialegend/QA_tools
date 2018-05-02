#-*- coding:utf-8 -*-

import requests

url = 'http://115.182.192.229'
port = 50280

def gm_order(roleid,func,id,count):
	global url
	global port

	dic = [roleid,func,id,count]

	for x in dic:
		



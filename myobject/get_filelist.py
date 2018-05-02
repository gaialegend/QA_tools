#-*-coding:utf-8 -*-

import os

path = os.getcwd() + '/package'

def get_downloadfile():
	global path
	d_path = path + '/download'
	#print os.listdir(d_path)
	pack_dic = {}
	for x in os.listdir(d_path):
		pack_dic[x] = os.path.abspath(x)
	print pack_dic
	return pack_dic




if __name__ == '__main__':
	get_downloadfile()
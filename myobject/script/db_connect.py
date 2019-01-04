#-*- coding:utf-8 -*-

import pymysql
import sys


# def check_shieldername(name):
# 	check_li = []
# 	check_name = list(name)
# 	for x in check_name:
# 		if 
reload(sys)

sys.setdefaultencoding("utf-8")
class Db_connect:
	def __init__(self,host,port,user,password,db):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
		self.charset = 'utf8'
		#self.filename = filename

	def connect(self):
		conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.password,db=self.db,charset=self.charset)
		cursor = conn.cursor()
		return cursor

	def execute(self,order):
		cursor = self.connect()
		effect_raw = cursor.execute(order)
		raw_all = cursor.fetchall()
		return raw_all

# def connect_bl2_gamedb(host,port,user,password,db):
# 	conn = pymysql.connect(host=host,port=port,user=user,passwd=password,db=db,charset='utf8')
# 	cursor = conn.cursor()
# 	effect_raw = cursor.execute('select')



if __name__ == '__main__':
	test_name = '古花'
	test1 = Db_connect('115.182.192.230',63306,'rootuser','yu@2015','bl2_gamedata4')
	#print type(test1)
	result = test1.execute('select role_name,character_id from user')
	# print type(result)
	# print len(result)
	# for x in result:
	# 	print x[0]
	# 	for i in list(x[0]):
	# 		print type(i)			
	# 		print i
	# 	print '--------------------------------'
	test_len = len(test_name.decode('utf-8'))
	#print test_len
	counter = 0
	for k in result:
		last_index = 0
		bCheck = True
		#print result
		for x in test_name.decode('utf-8'):
			#if x not in k[0]:
			#	break
			try:
				last_index = k[0].index(x, last_index) + 1
				#counter += 1
			except ValueError:
				#print '------------------'
				bCheck = False
				break
		if bCheck == True:
			print k
		# if counter == test_len:
		# 	print k[0]
		# counter = 0



#-*- coding:utf-8 -*-

import pymysql

db = pymysql.connect(host='115.182.192.230',user='rootuser',passwd='yu@2015',db='bl2_gamedata',port=63306,charset='utf8')

cursor = db.cursor()

data = cursor.execute('select * from user')
print data

one = cursor.fetchall()
print type(one)
for x in one:
	print x[8]
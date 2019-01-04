#-*- coding:utf-8 -*-

import db_connect
import shelderword
import csv

sheldername_dic = shelderword.shelderword('shieldword_cs.csv').load_file()
db_filename = 'db_list.csv'
shelderword_filename = 'shieldword_cs.csv'

def dbconnect():
	global db_filename
	dblist = []
	#db_detail = {}
	with open(db_filename,'r') as dbserver:
		reader = csv.DictReader(dbserver)
		for x in reader:
			print x
			dblist.append(x)
	return dblist

def rolename_check():
	dblist =dbconnect()
	shelderword_dic = shelderword.shelderword(shelderword_filename)
	check_rolename_lis = []

	for db in dblist:
		test_tar = db_connect.Db_connect(db['host'],int(db['port']),db['user'],db['passwd'],db['gamedata'])
		result = test_tar.execute('select role_name,character_id from user')
		if len(result) != 0:
			print db['gamedata'] + 'result get success'
		for k in result:
			last_index = 0
			bCheck = True
			for shword in shelderword_dic.load_file().values():
				for x in shword.decode('utf-8'):
					try:
						last_index = k[0].index(x,last_index) + 1
					except ValueError:
						bCheck = False
						break
				if bCheck:
					print k
					check_rolename_lis.append(k)
		print db['gamedata'] + 'check done'
	return check_rolename_lis




if __name__ == '__main__':
	rolename_check()


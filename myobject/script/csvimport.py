#-*-coding:utf-8 -*-

import db_connect
import csv


#csvdatabases = db_connect.Db_connect('localhost',None,'root','guan@2018','flaskdata')

#result = csvdatabases.execute('show tables')

class CsvTable:
	def __init__(self,filename):
		self.filename = filename
		self.localpath = 'csv/'
		self.host = 'localhost'
		self.user = 'root'
		self.passwd = 'guan@2018'
		self.database = 'flaskdata'


	def connect(self):
		csvdatabase = db_connect.Db_connect(self.host,None,self.user,self.passwd,self.database)
		return csvdatabase


	def create(self):
		csvdatabase = self.connect()
		with open(self.localpath+self.filename,'r') as csv_file:
			times = 0
			head = []
			body = []
			reader = csv.reader(csv_file)
			for x in reader:
				if times in range(1,2):
					head.append(x)
				else:
					body.append(x)
				times += 1
		return 
		#for key in head[0]:


		#order = 'create table if not exists '+self.filename.split('.')[0] + '('+ +')'


				




if __name__ == '__main__':
#-*- coding:utf-8 -*-

#import db_connect
import csv


class shelderword:
	def __init__(self,filename):
		self.filename = filename


	def load_file(self):
		shelderword_dic = {}
		count = 0
		file_name = self.filename
		with open(file_name,'r') as csv_file:
			reader = csv.reader(csv_file)
			for x in reader:
				if count <= 2:
					count += 1
					continue
				else:
					shelderword_dic[x[0]] = x[1]
		#print shelderword_dic
		return shelderword_dic









if __name__ == '__main__':
	
	tar = shelderword('shieldword_cs.csv')
	for x in tar.load_file().values():
		print x
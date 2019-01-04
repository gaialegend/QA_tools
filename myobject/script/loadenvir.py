#-*-coding:utf-8 -*-

import os
import csv
import Csvdata
class Loadyycsvfile:
	def __init__(self,dirlist):
		self.yy_csv_model = 'yy_csv'
		self.csv_model = 'csv'
		self.dir = 'envir'
		self.dirlist_yycsv = dirlist


	def loadcsvfile(self,model,target):
		basedir = os.getcwd()
		dirlist = os.listdir(os.getcwd())
		target_dir = ''
		#print dirlist
		if self.dir not in dirlist:
			#print 'oops'
			os.chdir(os.pardir)
			dirlist = os.listdir(os.getcwd())
			#print dirlist
		if self.dir in dirlist:
			#print 'find!'
			target_dir = os.getcwd() + '\\' + self.dir + '\\'
			#print '--------------------------------------'
			#print target_dir
		else:
			#print 'error, dont find'
			target_dir = ''
		target_detail = target_dir + model + '\\' + target
		#print target_detail
		with open(target_detail,'r') as csv_file:
			#reader = csv.DictReader(csv_file)
			csv_reader = Csvdata.Csvdata(csv_file)
			csv_reader.post()
			if csv_reader.get_en():
				print 'Success'
			else:
				print 'Error'
			# for row in reader:
			# 	print row
		os.chdir(basedir)
		return csv_reader

	def csv_readloop(self,model):
		result = {}
		switch = None
		if model == 'yy_csv':
			switch =self.yy_csv_model
		elif model == 'csv':
			switch =self.csv_model
		for x in self.dirlist_yycsv:
			#print x
			result[x] = self.loadcsvfile(switch,x)
		#print result
		return result

		



if __name__ == '__main__':
	tar = Loadyycsvfile(['item_consumable_cs.csv'])
	result = tar.csv_readloop('csv')
	print result['item_consumable_cs.csv'].csvdict
	print len(result['item_consumable_cs.csv'].csvdict)
	# 	for i in result[x].csvdict:
	# 		for k,v in i.iteritems():
	# 			print k
	# 			print v

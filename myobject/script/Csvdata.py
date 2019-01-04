#-*-coding:utf-8 -*-

import csv

class Csvdata:
	def __init__(self,csvfile):
		self.csvfile = csvfile
		self.csvreader = None
		self.csvdict = None
		self.csvdict_type = None
		self.csvdict_cn = None
		self.csvdict_type_cn = None

	def post(self):
		reader = csv.reader(self.csvfile)
		self.csvreader = reader
		return True

	def get_en(self):
		counter = 0
		if self.csvreader != None:
			self.csvdict = []
			dic_detail = {}
			keys_li = None
			keys_type = None
			for row in self.csvreader:
				# count = 0
				# while counter <3:
				# 	#print 'step'
				# 	#print counter
				# 	if counter == 1:
				# 		#中文这里是0
				# 		print '-----------------------------'
				# 		print row
				# 		keys_li = row
				# 		print 'this is keys_li'
				# 		print keys_li
				# 		for x in keys_li:
				# 			print x
				# 	elif counter ==2:
				# 		print '-------------------------------'
				# 		keys_type = row
				# 		print 'this is keys_type'
				# 		print keys_type
				# 		for x in keys_type:
				# 			print x
				# 	else:
				# 		#print 'error'
				# 		print counter
				# 		counter += 1
				# 		continue
				# 	counter +=1
				# 	continue
				if self.csvreader.line_num == 2:
					keys_li = row
				if self.csvreader.line_num == 3:
					keys_type = row
				if keys_li != None and keys_type != None:
					if self.csvdict == None and self.csvdict_type ==None:
						self.csvdict_type = dict(zip(keys_li,keys_type))
					dic = {}
				# print self.csvreader.line_num
				if self.csvreader.line_num > 3:
					# print count
					# print keys_li
					dic_detail = dict(zip(keys_li,row))
					# dic[row[0]] = dic_detail
					# print dic_detail
					self.csvdict.append(dic_detail)
					# self.csvdict.append(dic)
				# count += 1
			return True
		else:
			try:
				self.post()
				return self.get_en()
			except BaseException,e:
				print 'Failed'
				print e.message
				return False




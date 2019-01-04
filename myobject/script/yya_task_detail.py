#-*-coding:utf-8 -*-


import xlrd
import sys
import loadenvir

reload(sys)
sys.setdefaultencoding('utf-8')


class yya_task_detail:
	def __init__(self,workbookfile):
		self.raw_workbookfile = u'new任务配置.xlsx'
		self.raw_detail = None
		#yya_task
		self.workbookfile = workbookfile
		self.detail = None
		self.item = None
		self.checkfuncdic = {
			1087:self.yyatask_soulstone,

		}

	def yya_task_raw_detail_config(self):
		detail_dic = {}
		detail_dic_ = {}
		workbook = xlrd.open_workbook(self.raw_workbookfile)
		sheet2 = workbook.sheet_by_index(1)
		for x in range(sheet2.nrows):
			#print x
			if x != 0:
				detail_dic_ = {}
				detail_dic_['id'] = int(sheet2.row_values(x)[0])
				detail_dic_['name'] = sheet2.row_values(x)[1]
				detail_dic_['value'] = sheet2.row_values(x)[2]
				detail_dic_['instruction'] = sheet2.row_values(x)[3]
				detail_dic[int(sheet2.row_values(x)[0])] = detail_dic_
		self.raw_detail = detail_dic
		#print detail_dic
		return detail_dic

	def yya_task_detail_config(self):
		tar = loadenvir.Loadyycsvfile([self.workbookfile])
		result = tar.csv_readloop('yy_csv')
		#print result['quest_yya_task_s.csv'].csvdict
		self.detail = result['quest_yya_task_s.csv'].csvdict
		return result['quest_yya_task_s.csv']

	def yya_task_item_detail_config(self):
		itemidlis = {}
		tar = loadenvir.Loadyycsvfile(['item_consumable_cs.csv'])
		result = tar.csv_readloop('csv')
		#print type(result['item_consumable_cs.csv'].csvdict)
		#print result['item_consumable_cs.csv'].csvdict
		for x in result['item_consumable_cs.csv'].csvdict:
			itemidlis[x['ID']] = x
		#print len(itemidlis)
		#print itemidlis
		self.item = itemidlis
		return itemidlis

	def precheck(self):
		if self.item == None:
			item_dic = self.yya_task_item_detail_config()
		#print len(self.checkfuncdic)
		#print self.checkfuncdic.keys()
		raw_detail_dic = self.yya_task_raw_detail_config()
		#print raw_detail_dic
		#rawdata = raw_detail_dic[int(id)]
		detail_dic = self.yya_task_detail_config()
		#print rawdata
		for x in detail_dic.csvdict:
			#print x
			if int(x['CompleteType']) not in raw_detail_dic.keys():
				print 'error'
				print '----------------------------------------'
				print x['CompleteType']
				print 'not find in the rawdata'
			else:
				#print raw_detail_dic
				rawdata = raw_detail_dic[int(x['CompleteType'])]
				completettype = len(x['CompleteCoefficient'].split(';'))
				raw_completettype_len = len(rawdata['value'].split('；'))
				#elif ';' in rawdata['value']:
					#raw_completettype_len = len(rawdata['value'].split(';'))
				#elif len(rawdata['value'].split('；')) != 1:
					#print '------------------------------------------'
					#print 'split failed'
					#print rawdata['value']

				print '------------------------------------------'
				print x['CompleteType']
				print 'completettype = ' + str(completettype)
				print 'raw_completettype_len = ' + str(raw_completettype_len)
				print rawdata['value']
				print x['CompleteCoefficient']
				print len(rawdata['value'].split('；'))
				if completettype != raw_completettype_len:
					print 'value number error'
				elif len(self.checkfuncdic) != 0 and int(x['CompleteType']) in self.checkfuncdic.keys():
					self.checkfuncdic[int(x['CompleteType'])](x['QuestID'])
		return True


	#灵魂石任务 1087
	def yyatask_soulstone(self,id):
		if self.item != None:
			itemlist = self.item
		else:
			print 'error itemlist Null'
			return False
		print 'start check 1087'
		detail_dic = self.yya_task_detail_config()
		taskreward = detail_dic.csvdict
		
		return True














if __name__ == '__main__':
	tar = yya_task_detail('quest_yya_task_s.csv')
	tar.precheck()


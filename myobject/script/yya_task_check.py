#-*-coding:utf-8 -*-

import loadenvir
import time, datetime
import yya_task_detail
import csv
# class Task_check_yya:
# 	def __init__(self):
# 		self.checkfilelist = ['quest_yya_limit_s.csv','quest_yya_main_s.csv','quest_yya_month_s.csv','quest_yya_point_reward_s.csv','quest_yya_task_s.csv']

# 	def precheck(self,dirdict):
# 		#before check filename
# 		count = 0
# 		for x in dirdict.keys():
# 			if x in self.checkfilelist:
# 				count += 1

# 		if count == len(self.checkfilelist):
# 			return True
# 		else:
# 			return False

# 	def check_daytime(self,dirdict):
# 		yya_task_main = dirdict['quest_yya_main_s.csv']
		
class yya_task_check(object):
	"""docstring for yya_task_check"""
	def __init__(self):
		super(yya_task_check, self).__init__()

		self.csv = None
		self.item_csv = None
		self.maindata = None
		self.monthdata = None
		self.limitdata = None
		self.pointrewarddata = None
		self.taskdata = None
		self.itemdata = None


	def precheck(self):
		try:
			tar = loadenvir.Loadyycsvfile(['quest_yya_limit_s.csv','quest_yya_main_s.csv','quest_yya_month_s.csv','quest_yya_point_reward_s.csv','quest_yya_task_s.csv'])
			result = tar.csv_readloop('yy_csv')
			self.csv = result
			tar_item = loadenvir.Loadyycsvfile(['item_consumable_cs.csv'])
			self.item_csv = tar_item.csv_readloop('csv')
		except  BaseException,e:
			print e.message
			return False
		self.maindata = self.csv['quest_yya_main_s.csv'].csvdict
		self.monthdata = self.csv['quest_yya_month_s.csv'].csvdict
		self.limitdata = self.csv['quest_yya_limit_s.csv'].csvdict
		self.pointrewarddata = self.csv['quest_yya_point_reward_s.csv'].csvdict
		self.taskdata = self.csv['quest_yya_task_s.csv'].csvdict
		self.itemdata = self.item_csv['item_consumable_cs.csv'].csvdict
		return True

	def yya_main_check_timecheck(self):
		print '----------------time--check--------------------'
		for x in self.maindata:
			timeArray_start = time.strptime(x['Start'],"%Y.%m.%d %H:%M:%S")
			timeArray_end = time.strptime(x['End'],"%Y.%m.%d %H:%M:%S")
			timeStamp_start = int(time.mktime(timeArray_start))
			timeStamp_end = int(time.mktime(timeArray_end))
			if timeStamp_end < timeStamp_start:
				print '-----------------------------'
				print x['ID']
				print x['Start']
				print x['End']
		return True

	def yya_main_check_Month(self):
		print '------------------start---main-check------------------'
		month_id = []
		#month_detail = []
		dict_month = {}
		for i in self.monthdata:

			dict_month[i['ID']] = i
			if len(dict_month) != 0:
				month_id.append(i['ID'])
		#print month_id
		#print dict_month
		for x_main in self.maindata:
			month = x_main['Month'].split(';')
			#print month_detail
			for i in month:
				if i not in month_id:
					print '-------------Error not in month------------------------'
					print x_main['ID']
					print i
					print '--------------------------------------------'
				else:
					month_starttime = time.strptime(x_main['Start'], "%Y.%m.%d %H:%M:%S")
					month_endtime = time.strptime(x_main['End'], "%Y.%m.%d %H:%M:%S")
					if month_endtime < month_starttime:
						print '----------------Error please check main time------------------------'
						print dict_month[i]
						print '----------------------------------------'
					if month_endtime <time.strptime(dict_month[i]['End'], "%Y.%m.%d %H:%M:%S") or month_starttime > time.strptime(dict_month[i]['Start'], "%Y.%m.%d %H:%M:%S"):
						print '-------------Error please check month time ----------------------'
						print dict_month[i]
						print '-------------Start time main-------------------------------------'
						print x_main['Start']
						print '-------------Start time month------------------------------------'
						print dict_month[i]['Start']
						print '-------------End time main---------------------------------------'
						print x_main['End']
						print '-------------End time month--------------------------------------'
						print dict_month[i]['End']
						print '-----------------------------------------------------------------'
						print '----------------------------------------'
		print '-------------Month_main----check-----End---------'
		return True

	def yya_main_check_Reward(self):

		#reward_data = self.pointrewarddata
		reward_dic = {}
		for x_main in self.maindata:
			reward_dic[x_main['ID']] = x_main['Reward'].split(';')

		#print reward_dic
		pointreward_li = []
		pointreward_dic = {}
		for x_reward in self.pointrewarddata:
			pointreward_li.append(x_reward['ID'])
			pointreward_dic[x_reward['ID']] = x_reward
		print '-------------start----Reward---check--------------------'
		for k,v in reward_dic.items():
			if not set(v).issubset(pointreward_li):
				print '--------------------find error------------------'
				print k
			else:
				reward_point_li = []
				for i in v:
					reward_point_li.append(pointreward_dic[i]['Point'])
				if reward_point_li <= 1000:
					print '-------------------warning---score too small----'
		print '-------------Reward---check----end----------------------'
		return True

	def yya_reward_check_item(self):
		pointreward_dic = {}
		itemid_dic = {}
		if len(pointreward_dic) == 0:
			for x_reward in self.pointrewarddata:
				pointreward_dic[x_reward['ID']] = x_reward
		for item_detail in self.itemdata:
			item_detail_dic = {}
			item_detail_dic['ID'] = item_detail['ID']
			item_detail_dic['Type'] = item_detail['Type']
			itemid_dic[item_detail['ID']] = item_detail_dic
		print '-------------start----Reward-item--check--------------------'
		for reward_item in pointreward_dic:
			item_list = []
			#print list(pointreward_dic[reward_item]['Reward'])
			if ';' in list(pointreward_dic[reward_item]['Reward']):
				item_list = pointreward_dic[reward_item]['Reward'].split(';')

			else:
				item_list.append( pointreward_dic[reward_item]['Reward'])
			#print reward_item,item_list
			for x in item_list:
				item_d = x.split('|')
				if len(item_d) != 3:
					print '-----------------error---------------------------'
					print reward_item,item_list,item_d
				else:
					it_type = item_d[0]
					it_item = item_d[1]
					it_count = item_d[2]
				if it_item not in itemid_dic.keys():
					print '---------------------error----------------------'
					print '----------------not---find---in--itemtable------'
					print it_item
				else:
					tar_item_type = itemid_dic[it_item]['Type']
					if it_type != tar_item_type:
						print '-----------------error---------------------'
						print '---------item--type--error-----------------'
		print '-------------Reward_item---check----end----------------------'
		return True

	def yya_task_check(self):
		precheck_taskid = []
		with open('precheckid.csv','r') as textfile:
			dict_csv = csv.DictReader(textfile)
			for i in dict_csv:
				try:
					print i.values()
					int(i.values()[0])
					precheck_taskid.append(int(i.values()[0]))
				except:
					continue

		print precheck_taskid
		itemid_dic = {}
		for item_detail in self.itemdata:
			item_detail_dic = {}
			item_detail_dic['ID'] = item_detail['ID']
			item_detail_dic['Type'] = item_detail['Type']
			itemid_dic[item_detail['ID']] = item_detail_dic
		for x in self.taskdata:
			if len(x['Reward1'].split(';')) == 3 and x['Reward1'].split(';')[1] not in itemid_dic.keys():
				print '--------------------Error---reward--error---------'
				print x['Reward1'].split(';')[1]

		task_dic = yya_task_detail.yya_task_detail().yya_task_detail_config()
		print task_dic

		return True


















if __name__ == '__main__':
	tar = yya_task_check()
	if tar.precheck():
		tar.yya_main_check_timecheck()
		#tar.yya_main_check_Month()
		#tar.yya_main_check_Reward()
        #tar.yya_reward_check_item()
        tar.yya_task_check()




		


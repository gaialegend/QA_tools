#-*- coding:utf-8 -*-

import csv
import xml.dom.minidom
import time
import Itemdata
from decimal import Decimal
from decimal import getcontext
import sys
import io
import xml
reload(sys)
#sys.setdefaultencoding( "gb18030" )
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
sys.setdefaultencoding("utf-8")
def xml2dic(filename):
	card_name_dic ={}
	DOMTree = xml.dom.minidom.parse(filename)
	#print 'hello'
	collection = DOMTree.documentElement
	#print collection
	card_name = collection.getElementsByTagName("item")
	for x in card_name:
		# print x
		# print x.getAttribute('id')
		#print type(x.getAttribute('text'))
		#print x.getAttribute('text')
		card_name_dic[x.getAttribute('id')] = x.getAttribute('text')
	return card_name_dic

# def xml2dic_dup(filename):
# 	dup_name_dic = {}
# 	DomTree = xml.dom.minidom.parse(filename)
# 	collection = DomTree.documentElement
# 	dup_name = collection.getElementsByTagName("")

def get_item_detail():
	with open('item_consumable_cs','rb') as itemconsumable:
		item_dic = xml2dic('disstr_item.xml')
		reader = csv.reader(itemconsumable)
		for i in reader:
			item_detail = Itemdata()

	pass


def get_card_name(card_id):
	name_dic = {}
	card_main_dic = {}
	card_name_dic = {}

	with open('card_name.csv','r') as name_csvflie:
		reader = csv.reader(name_csvflie)
		for i in reader :
			name_dic[i[0]] = i[1]

	with open('card_cs.csv','r') as card_main:
		c_reader = csv.reader(card_main)
		for x in c_reader:
			card_main_dic[x[0]] = x[7]
	#print card_main_dic[card_id]
	#name_dic = xml2dic('disstr_card.xml')
	#print card_name_dic[card_id]
	card_name = name_dic[card_main_dic[card_id]]
	print str(card_name)
	print type(str(card_name))
	return str(card_name)

def get_dup_name(dup_id=None):
	name_dic = {}
	dup_dic = {}

	with open('map_duplicate_cs.csv','r') as dup_csvfile:
		reader = csv.reader(dup_csvfile)
		for i in reader:
			name_dic[i[0]] =i[3]
	with open('multiple_duplicate_cs.csv','r') as multdup_csvfile:
		reader = csv.reader(multdup_csvfile)
		for i in reader:
			name_dic[i[0]] = i[1]
	dup_dic = xml2dic('disstr_dup.xml')
	#print dup_dic

	if dup_id != None:
		try:
			print type(dup_id)
			#print name_dic[dup_id]
			#print dup_dic[name_dic[dup_id]]
			return [{'id':dup_id,'dup_name':dup_dic[name_dic[dup_id]]}]
		except KeyError:
			print '---------------------------------------'
			try:
				dup_dic_turn = {value:key for key,value in dup_dic.items()}
				#name_dic_turn = {value:key for key,value in name_dic.items()}
				dup_li = []
				for x in dup_dic_turn.keys():
					#print x
					if dup_id in x or dup_id == x:
						#print name_dic_turn[dup_dic_turn[x]]
						#print list(name_dic.values())
						print dup_dic_turn[x]
						#print dup_dic_turn[x] in list(name_dic.values())
						print '----------------------------------------'
						#print list(name_dic.values()).index(dup_dic_turn[x])
						try:
							print x
							result = {x:list(name_dic.keys())[list(name_dic.values()).index(dup_dic_turn[x])]}
							dup_li.append(result)
						except ValueError,e:
							print e
							continue
				print dup_li
				return dup_li
			#print 'oops'
			#print name_dic
			except (),e:
				print e.message
				print 'oops'
				return None
	else:
		print name_dic
	return None

def get_card_rank(card_id):
	rank_dic = {}
	rank = {'1':'R','2':'SR','3':'SSR','0':'N'}
	with open('card_cs.csv','r') as card_main:
		c_reader = csv.reader(card_main)
		for x in c_reader:
			if x[69] not in ['SSR','int']:
				#print x[69]
				r_rank = rank[str(x[69])]
				rank_dic[x[0]] = r_rank
	card_star = rank_dic[card_id]
	#print card_star
	return card_star

def report(card_result_dic,count,type=None):
	dic = card_result_dic
	filename=str(time.time()) + '.csv'
	with open(filename,'wb') as reporter:
		myreporter = csv.writer(reporter,dialect='excel')
		myreporter.writerow(['rank','name_dic','count','chance'])
		for k,v in dic.items():
			chance = str(Decimal(v)/Decimal(count)*100)
			card_name = get_card_name(str(k))
			card_rank = get_card_rank(str(k))
			myreporter.writerow([card_rank,card_name,str(v),chance])
		reporter.close()
	return filename

def get_item_name_dic():
	dom = xml.dom.minidom.parse('disstr_item.xml')
	root = dom.documentElement
	itemid = root.getElementsByTagName('item')
	item_name_dic = {}
	for x in itemid:
		item_name_dic[x.getAttribute('id')]=x.getAttribute('text')
	#print item_name_dic
	return item_name_dic

def get_item_dic():
	print '----------------------func:get_item_dic---------------------------------'
	item_name = get_item_name_dic()
	with open('item_consumable_cs.csv','rb') as item_consumable:
		item_con = csv.reader(item_consumable)
		item_dic = []
		item_id_dic = {}
		item_name_dic = {}
		for x in item_con:
			if str(x[1]) != '5':
				item_detail = {}
				item_detail_2 = {}
				#print x
				try:
					#print item_name[x[4]]		
					item_detail['name'] = item_name[x[4]]
					# item_detail['type'] = x[1]
					# item_dic[x[0]] = x[4]
					# item_dic[x[0]] = item_detail
				except KeyError:
					item_detail['name'] = 'Null'
				item_detail['type'] = x[1]
				#item_dic[x[0]] = x[4]
				item_id_dic[x[0]] = item_detail

				item_detail_2['id'] = x[0]
				item_detail_2['type'] = x[1]
				try:
					__itemname__ = item_name[x[4]]
					item_name_dic[__itemname__] = item_detail_2
				except KeyError:
					continue
	item_dic.append(item_id_dic)
	item_dic.append(item_name_dic)
	# for _test_ in item_dic:
	#  	print _test_
	#print item_dic
	#print type(item_dic)
	return item_dic

 

# def get_item_name(element):
# 	xml2name = get_item_name_dic()
# 	csv2id = get_item_dic()
# 	#print xml2name[csv2id[str(element)]]
# 	try:
# 		#item_name = xml2name[csv2id[]]
# 		item_name = xml2name[csv2id[str(element)]]
# 	except:
# 		item_name = '未能找到对应道具名,请确认id或者更新配置表'
# 	print item_name
# 	return item_name

def get_item_name(element):
	item_name_dic = get_item_dic()
	print '---------------func:get_item_name------------------------'
	print element
	item_dic = item_name_dic[0]
	#print item_dic
	print type(item_dic)
	print item_dic[str(element)]
	item_detail = [item_dic[str(element)]['type'],item_dic[str(element)]['name']]
	#item_detail = [[item_name_dic[0]]['type'],[item_name_dic][0]['name']]
	print item_detail
	for x in item_detail:
		print x
	return item_detail


# def get_item_id(name):
# 	xml2name = get_item_name_dic()
# 	csv2id = get_item_dic()
# 	name2xml = dict(zip(xml2name.values(),xml2name.keys()))
# 	id2csv = dict(zip(csv2id.values(),csv2id.keys()))
# 	item_id = ''
# 	try:
# 		item_id = id2csv[name2xml[name.decode('utf-8')]]
# 	except KeyError:
# 		li = []
# 		for x in name2xml.keys():
# 			if name.decode('utf-8') in x:
# 				li.append(x)
# 		if len(li) != 0:
# 			item_id = {}
# 			for i in li:
# 				try:
# 					item_id[i]=id2csv[name2xml[i.decode('utf-8')]]
# 				except KeyError:
# 					#print '有未找到对应的道具,i =' + i
# 					print 'find failed'
# 		else:
# 			item_id ='未能找到对应道具名'
# 	print type(item_id)
# 	# if type(item_id) == type({}):		
# 	# 	for a in item_id.keys():
# 	# 		print a
# 	return item_id

def get_item_id(name):
	item_name_dic = get_item_dic()[1]
	#print item_name_dic
	item_id = ''
	item_type = None
	lis = []
	try:
		# item_id = item_name_dic[name.decode('utf-8')]['id']
		# item_type = item_name_dic[name.decode('utf-8')]['type']
		#print name.decode('utf-8')
		item_detail = item_name_dic[name.decode('utf-8')]
		print '------------------------------------------------'
		print item_detail
		if (item_detail['name'] == name.decode('utf-8') or name.decode('utf-8') in x) and (item_detail['type'] != 5):
			li.append(x)
		lis.append(item_detail)
	except KeyError,e:
		print e
		print '-----------------------------1-----------------'
		li = []
		#print len(item_name_dic.keys())
		for x in item_name_dic.keys():
			#print type(x)
			if name.decode('utf-8') in x:
				print x
				li.append(x)
		#print li
		if len(li) != 0:
			#print 'len(li)'
			#print len(li)
			tem_id = {}
			for i in li:
				print 'yo,i am i '
				print type(i)
				print i
				try:
					# item_id = item_name_dic[i.decode('utf-8')]['id']
					# item_type = item_name_dic[i.decode('utf-8')]['type']
					item_detail = item_name_dic[i.decode('utf-8')]
					item_detail['name'] = i.decode('utf-8')
					lis.append(item_name_dic[i.decode('utf-8')])
				except KeyError:
					print 'find failed'
	if len(lis) == 0:
		Null_detail = {'type':'0','id':'0','name':'Null'}
		lis.append(Null_detail)
	# for _test_ in lis:
	# 	print _test_['name'].decode('utf-8')
	# 	print _test_['id']
	# 	print _test_['type'].decode('utf-8')
	print lis
	return lis



if __name__ == '__main__':
	get_dup_name('魔能机甲')
	pass
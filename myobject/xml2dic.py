#-*-coding:utf-8 -*-

import xml.dom.minidom
import os
import sys
import csv

reload(sys)
sys.setdefaultencoding( "utf-8" )
# path = os.getcwd()

#with open(path+disstr_item.xml) as myfile:

dom = xml.dom.minidom.parse('disstr_item.xml')

root = dom.documentElement

itemid = root.getElementsByTagName('item')
item_name_dic = {}
for x in itemid:
	# print x.getAttribute('id')
	# print x.getAttribute('text')
	item_name_dic[x.getAttribute('id')]=x.getAttribute('text')

# for i in item_name_dic.keys(): 
# 	print i + ','+item_name_dic[i]

with open('item_consumable_cs.csv','rb') as item_consumable:
	item_file = csv.reader(item_consumable)
	item_dic = {}
	for i in item_file:
		
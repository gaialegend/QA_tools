#-*-coding:utf-8 -*-

class Itemdata(object):
	def __init__(self,item_id,item_type,item_name):
		self.item_id = item_id
		self.item_type = item_type
		self.item_name = item_name

	def get_item_id(self):
		return self.item_id

	def get_item_type(self):
		return self.item_type

	def get_item_name(self):
		return self.item_name
#-*-coding:utf-8 -*-

class test_class(object):
	def __init__(self):
		self.score = 65
		self.name = 'erjia'



if __name__ == '__main__':
	d = test_class.__dict__
	student = test_class()
	print vars(student)
	print type(vars(student))

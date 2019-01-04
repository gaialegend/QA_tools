#-*-coding:utf-8 -*-

class Loop(object):
	"""docstring for Loop"""
	def __init__(self, *params):
		super(Loop, self).__init__()
		li = []
		for x in params:
			li.append(x)
		self.loop = li

	def insert(self,element):
		self.loop.append(element)
		return True

	def delete(self,element):
		try:
			self.loop.pop(element)
			return True
		except e:
			print e.message 
			print 'Failed'
			return False

	def run(self,func,*params):
		if len(params) != 0:
			for x in params:
				func()

		return True




	# def run_loop(self):
	# 	for x in self.loop:
			



if __name__ == '__main__':
	test = Loop(1,2,34)
	#print test.loop
	test.insert(23)
	print test.loop
	test.delete(23)
	print test.loop







		

#-*-coding:utf-8 -*-

class CountList:
	def __init__(self,*args):
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)),0)

	def __len__(self):
		return len(self.values)

	def __getitem__(self,key):
		self.count[key] += 1
		return self.values[key]


if __name__ == '__main__':
	c1 = CountList(1,3,5,7,9)
	print c1.count
	print c1.values
	print c1[1]
	#print range(len(c1.values))
	#print c1.count
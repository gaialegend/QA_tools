#-*-coding:utf-8 -*-

def test(*paragram):
	print paragram
	for x in paragram:
		print x


if __name__ == '__main__':
	test(0,2,3,4)
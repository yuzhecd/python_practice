#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 21:30:32
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Test_2:
	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')

def main():
	test = Test_2('hello')
	test._Test_2__bar()
	print(test._Test_2__foo)

if __name__ == '__main__':
	main()

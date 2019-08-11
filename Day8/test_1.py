#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 21:26:58
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Test_1:
	def __init__(self, foo):
		self.__foo = foo

	def __bar(self):
		print(self.__foo)
		print('__bar')

def main():
	test = Test_1('hello')
#	test.__bar()
	print(test.__foo)

if __name__ == '__main__':
	main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 20:28:15
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def main():
	list_1 = [1, 3, 5, 7, 100]
	print(list1)
	list_2 = ['hello'] * 5
	print('the length of list_1 is {}'.format(len(list_1))
	print(list_2)
	print(list_1[1])
	print(list_1[4])

	list_1.append(200)
	list_1.insert(1, 400)
	list_1 += [1000, 2000]
	print(list_1)
	print('the length of list_1 is {}'.format(len(list_1)))
	


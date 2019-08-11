#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-04 20:54:55
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def max_compare(x):
	(x[0], x[1]) = (x[1], x[0]) if x[0] < x[1] else (x[0], x[1])
	for middle in range(2, len(x)):
		if x[middle] > x[0]:
			x[1] = x[0]
			x[0] = x[middle]
		elif x[middle] > x[1]:
			x[1] = x[middle]

	return x[0], x[1]

if __name__ == '__main__':
	x = list(input('Please input a list: \n'),)
	max_x, littlemax_x = max_compare(x)
	print('The max and the next of x is {} and {}'.format(max_x, littlemax_x))

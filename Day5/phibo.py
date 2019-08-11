#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 11:14:29
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def fun(n):
	if n <= 2:
		return 1
	else:
		a = fun(n-1)
		b = fun(n-2)
		return a + b 

if __name__ == '__main__':
	number = int(input("Please input a number: "))
	phi = fun(number)
	print("Phi is %d" % phi)
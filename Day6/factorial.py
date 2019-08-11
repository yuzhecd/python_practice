#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-28 20:42:39
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def factorial(num):
	"""
	calculate factorial
	"""

	result = 1
	for n in range(1, num + 1):
		result *= n
	return result

m = int(input("m = "))
n = int(input("n = "))

print("the factorial of m and n is {}".format(factorial(m) // factorial(n) // factorial(m - n)))


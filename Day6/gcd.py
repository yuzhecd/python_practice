#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 19:33:59
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def gcd(x, y):
	(x, y) = (y, x) if x > y else (x, y)
	for factor in range(x, 0, -1):
		if x % factor == 0 and y % factor == 0:
			return factor


def lcm(x, y):
	return x * y // gcd(x, y)

if __name__ == '__main__':
	x = int(input("x = "))
	y = int(input("y = "))
	gcd_return = gcd(x, y)
	lcm_return = lcm(x, y)
	print("the gcd of x and y is {}, and the lcm is {}".format(gcd_return, lcm_return))


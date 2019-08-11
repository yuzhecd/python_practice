#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 19:44:21
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

x = int(input('x = '))
y = int(input('y = '))
if x > y:
	x, y = y, x

for factor in range(x, 0, -1):
	if x % factor == 0 and y % factor == 0:
		print("The greatest common divisor of %d and %d is %d " % (x, y, factor))
		print("The lowest common multiple of %d and %d is %d " % (x, y, x * y // factor))
		break
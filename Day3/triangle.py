#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 19:54:03
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and a + c > b:
	print('三角形周长为： %f' % (a + b + c))
	p = (a + b + c) / 2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print('三角形面积为： %f' % (area))
else:
	print('不能构成三角形')
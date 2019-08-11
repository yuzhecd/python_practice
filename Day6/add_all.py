#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 19:09:52
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def add(*args):
	total = 0
	for val in args:
		total += val
	return total

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 8, 9))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-28 20:52:24
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from random import randint

def roll_dice(n=2):
	"""
	roll dice
	n is the number of dice
	return the sum of count
	"""

	total = 0
	for _ in range(n):
		total += randint(1, 6)
	return total 

def add(a=0, b=0, c=0):
	return a + b + c

print(roll_dice())
print(roll_dice(n=3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=50, a=100, b=200))

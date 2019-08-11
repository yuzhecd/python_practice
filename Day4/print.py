#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 19:51:01
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

row  = int(input("Please input the number of row: "))
for i in range(row):
	for _ in range(i + 1):
		print("*", end='')
	print()

for i in range(row):
	for j in range(row):
		if j < row - i - 1:
			print(" ", end="")
		else:
			print("*", end="")
	print()

for i in range(row):
	for _ in range(row - i - 1):
		print(" ", end='')

	for _ in range(2 * i + 1):
		print("*", end='')
	print()
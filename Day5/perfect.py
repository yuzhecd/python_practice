#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 09:47:03
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

for number in range(1, 100):
	count = 0
	for i in range(1, number):
		if number % i == 0:
			count += i
	if count == number:
		print("%d is a perfect number" % count)

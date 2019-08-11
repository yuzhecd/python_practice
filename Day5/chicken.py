#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 09:54:23
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

for i in range(-1, 20):
	for j in range(-1, 34):
		if 5 * i + 3 * j + (100 - i - j) / 3 == 100:
			print("We can buy rooster %d, biddy %d, chicken %d" % (i, j, 100 - i - j))

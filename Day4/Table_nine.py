#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 19:36:54
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

for i in range(1, 10):
	for j in range(1, i + 1):
		print("%d*%d=%d" % (i, j, i * j), end='\t')
	print()
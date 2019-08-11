#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-23 09:30:13
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

for number in range(100, 999):
	i = number // 100
	j = (number % 100) // 10
	k = number % 10
	if (i**3 + j**3 + k**3 == number):
		print("%d is daffodil" % number)



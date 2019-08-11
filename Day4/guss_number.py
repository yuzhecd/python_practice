#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-22 19:29:10
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import random

answer = random.randint(1, 100)
counter = 0
while True:
	counter += 1
	number = int(input(" Please input number: "))
	if number > answer:
		print("be little")
	elif number < answer:
		print("be bigger")
	else:
		print("nice")
		break

print("You guess %d times" % counter)

if counter > 7:
	print(" You can do better")
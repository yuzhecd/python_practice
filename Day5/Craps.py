#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-27 19:41:31
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import random

dice_a = random.randint(1, 7)
dice_b = random.randint(1, 7)

print("The number of dice a is %d" % dice_a)
print("The number of dice b is %d" % dice_b)

if dice_a + dice_b == 7 or dice_a + dice_b == 11:
	print("Player win")
elif dice_a + dice_b == 2 or dice_a + dice_b == 3 or dice_a + dice_b == 12:
    print("Player lose")
else:
	middle_number = dice_a + dice_b
	while True:
		dice_c = random.randint(1, 7)
		dice_d = random.randint(1, 7)
	
		if dice_c + dice_d == middle_number:
			print("Player win, the sum is %d" % (dice_c + dice_d))
			break
		elif dice_c + dice_d == 7:
			print("Player lose, the sum is %d" % (dice_c + dice_d))
			break
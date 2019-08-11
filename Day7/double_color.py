#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 17:56:17
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from random import randrange, randint, sample

def display(balls):
	"""
	output the number of double color balls
	"""
	for index, ball in enumerate(balls):
		if index == len(balls) - 1:
			print('|', end=' ')
		print('%02d' % ball, end=' ')
	print()

def random_select():
	"""
	have a list of randomly
	"""

	red_balls = [x for x in range(1, 34)]
	selected_balls = []
	selected_balls = sample(red_balls, 6)
	selected_balls.sort()
	selected_balls.append(randint(1, 16))
	return selected_balls

def main():
	n = int(input('the number you input: '))
	for _ in range(n):
		display(random_select())

if __name__ == '__main__':
	main()
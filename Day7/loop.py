#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 21:01:48
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def main():
	persons = [True] * 30
	counter, number, index = 0, 0, 0
	while counter < 15:
		if persons[index]:
			number += 1
			if number == 9:
				persons[index] = False
				counter += 1
				number = 0
		index += 1
		index %=30
	for person in persons:
		print('Yes' if person else 'No', end=' ')

if __name__ == '__main__':
	main()

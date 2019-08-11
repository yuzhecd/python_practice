#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-29 19:43:09
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def is_palindrome(num):
	temp = num
	total = 0
	while temp > 0:
		total = total * 10 + temp % 10
		temp //= 10
	return total == num

def is_prime(num):
	for factor in range(2, num):
		if num % factor == 0:
			return False
	return True if num != 1 else False

if __name__ == '__main__':
	num = int(input('Please input an interger: '))
	if is_palindrome(num) and is_prime(num):
		print('{} is palindrome and prime.'.format(num))
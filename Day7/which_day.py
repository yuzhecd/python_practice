#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-06 17:30:44
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def is_leap_year(year):
	"""
	judge if it is a leap year
	"""

	return year % 4 == 0 and year % 100 !=0 or year % 400 == 0

def which_day(year, month, day):
	days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
	[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]][is_leap_year(year)]
	total = 0
	for index in range(month - 1):
		total += days_of_month[index]
	return total + day

def main():
 	print(which_day(1980, 11, 28))

if __name__ == '__main__':
	main()
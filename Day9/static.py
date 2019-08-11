#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-20 20:39:50
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from math import sqrt

class Triangle(object):

	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c

	@staticmethod
	def is_valid(a, b, c):
		return a + b > c and b + c > a and a + c > b

	def perimeter(self):
		return self._a + self._b + self._c

	def area(self):
		half = self.perimeter() / 2
		return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
	a = int(input('please input a: '))
	b = int(input('please input b: '))
	c = int(input('please input c: '))

	if Triangle.is_valid(a, b, c):
		t = Triangle(a, b, c)
		print('The perimeter of Triangle is {}'.format(t.perimeter()))
		print('The area of Triangle is {}'.format(t.area()))
	else:
		print('Can not be a Triangle')

if __name__ == '__main__':
	main()
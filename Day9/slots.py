#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-19 16:44:50
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Person(object):
	# only '_name', '_age', '_gender' attributes
	__slots__ = ('_name', '_age', '_gender')

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, age):
		self._age = age

	def play(self):
		if self._age <= 16:
			print('%s is playing' % self._name)
		else:
			print('%s is studying' % self._name)

def main():
	person = Person('James', 15)
	person.play()
	person.age = 33
	person.play()
	person._gender = 'man'
	print(person._gender)
	person.is_tall = True

if __name__ == '__main__':
	main()
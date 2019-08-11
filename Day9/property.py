#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-19 11:52:59
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Person(object):

	def __init__(self, name, age):
		self._name = name
		self._age = age

	# getter
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
			print('{} is playing fly.'.format(self._name))
		else:
			print('{} is studying.'.format(self._name))

def main():
	person = Person('James', 24)
	person.play()
	person.age = 13
	person.play()
	person.name = 'welsy'

if __name__ == '__main__':
	main()

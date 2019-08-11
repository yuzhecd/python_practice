#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 20:00:53
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
	"""
	Pet
	"""

	def __init__(self, nickname):
		self._nickname = nickname

	@abstractmethod
	def make_voice(self):
		"""
		making voice
		"""
		pass

class Dog(Pet):
	"""
	Dog
	"""

	def make_voice(self):
		print('{} is making voice of w...w...'.format(self._nickname))

class Cat(Pet):
	"""
	Cat
	"""

	def make_voice(self):
		print("{} is making voice of m...m...".format(self._nickname))


def main():
	pets = [Dog('Tom'), Cat('Jack'), Dog('Tommy')]

	for pet in pets:
		pet.make_voice()

if __name__ == '__main__':
	main()

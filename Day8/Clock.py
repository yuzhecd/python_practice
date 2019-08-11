#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 21:47:53
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Clock(object):
	def __init__(self, hour=0, minute=0, second=0):
		self._hour = hour
		self._minute = minute
		self._second = second

	def run(self):
		self._second += 1
		if self._second == 60:
			self._second = 0
			self._minute += 1
			if self._minute == 60:
				self._minute = 0
				self._hour += 1
				if self._hour == 24:
					self._hour = 0

	def show(self):
		print('Time is {}:{}:{}'.format(self._hour, self._minute, self._second))



	def main():
		clock = Clock(23, 59, 56)
		clock.show()
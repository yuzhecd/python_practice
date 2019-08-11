#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-20 20:54:47
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from time import time, localtime, sleep

class Clock(object):
	""" numerical clock
	"""
	def __init__(self, hour=0, minute=0, second=0):
		self._hour = hour
		self._minute = minute
		self._second = second

	@classmethod
	def now(cls):
		ctime = localtime(time())
		return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

	def run(self):
		"""
		run
		"""
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
		"""
		show the time 

		"""
		return '%02d:%02d:%02d' % \
		(self._hour, self._minute, self._second)

def main():
	clock = Clock.now()
	print('Time is {}'.format(clock.show()))
	for i in range (60):
		sleep(1)
		print('Time is {}'.format(Clock.now().show()))

if __name__ == '__main__':
	main()

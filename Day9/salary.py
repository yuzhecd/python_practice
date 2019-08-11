#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-11 22:09:53
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
	"""
	employee
	"""
	def __init__(self, name):
		"""
		init method

		"""
		self._name = name

	@property
	def name(self):
		return self._name

	@abstractmethod
	def get_salary(self):
		"""
		return the salary employee get
		"""
		pass

class Manager(Employee):
	"""
	Manager
	"""

	def get_salary(self):
		return 15000.0

class Programmer(Employee):
	"""
	Programmer
	"""

	def __init__(self, name, working_hour=0):
		super().__init__(name)
		self._working_hour = working_hour

	@property
	def working_hour(self):
		return self._working_hour
	
	@working_hour.setter
	def working_hour(self, working_hour):
		self._working_hour = working_hour if working_hour > 0 else 0

	def get_salary(self):
		return 150.0 * self._working_hour

class Saleman(Employee):
	"""
	Saleman
	"""
	def __init(self, name, sale=0):
		super().__init(name)
		self._sale = sale

	@property
	def sale(self):
		return self._sale
	
	@sale.setter
	def sale(self, sale):
		self._sale = sale if sale > 0 else 0

	def get_salary(self):
		return 1200.0 + self._sale * 0.05

def main():
	emps = [
			Manager('James'), Programmer('Tom'),
			Manager('Jack'), Saleman('Alisy')]

	for emp in emps:
		if isinstance(emp, Programmer):
			emp.working_hour = int(input("Please input {}'s working hour of this month: ".format(emp.name)))
		elif isinstance(emp, Saleman):
			emp.sale = float(input("Please input {}'s sale of this month: ".format(emp.name)))

		print("{}'s salary of this month is {}".format(emp.name, emp.get_salary()))

if __name__ == '__main__':
	main()
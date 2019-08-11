#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-01 19:33:05
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Person(object):
	"""
	People
	"""

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
		print('{} is having fun.'.format(self._name))

	def watch(self):
		if self._age >= 18:
			print('{} is watching football.'.format(self._name))
		else:
			print('{} is studying.'.format(self._name))

class Student(Person):
	"""
	student
	"""

	def __init__(self, name, age, grade):
		super().__init__(name, age)
		self._grade = grade

	@property
	def grade(self):
		return self._grade
	@grade.setter
	def grade(self, grade):
		self._grade = grade

	def study(self, course):
		print("{} is in {} and studies {}.".format(self._name, self._grade, course))

class Teacher(Person):
	"""
	Teacher
	"""

	def __init__(self, name, age, title):
		super().__init__(name, age)
		self._title = title

	@property
	def title(self):
		return self._title
	
	@title.setter
	def title(self, title):
		self._title = title

	def teach(self, course):
		print("{} is teaching {}".format(self._name, course))

def main():
	stu = Student('James', 15, 'grade3')
	stu.study('math')
	stu.watch()
	t = Teacher('Tom', 33, 'professor')
	t.teach('python')
	t.watch()


if __name__ == '__main__':
	main()
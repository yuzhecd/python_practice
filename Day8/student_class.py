#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-09 21:17:50
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def study(self, course_name):
		print('{} is studying {}'.format(self.name, course_name))

	def watch_movie(self):
		if self.age < 18:
			print('{} is only can see bear appears'.format(self.name))
		else:
			print('{} can see what you want to see.'.format(self.name))

def main():
	student_1 = Student('James', 26)
	student_2 = Student('Wesely', 11)
	student_1.study('Python')
	student_1.watch_movie()
	student_2.study('Math')
	student_2.watch_movie()

if __name__ == '__main__':
	main()
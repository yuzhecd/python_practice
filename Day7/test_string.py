#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 16:48:39
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def main():
	str1 = 'hello world'
	print(len(str1))
	print(str1.capitalize())
	print(str1.upper())
	print(str1.find('or'))
	print(str1.find('shit'))
	print(str1.index('or'))
#	print(str1.index('shit'))
	print(str1.startswith('He'))
	print(str1.startswith('hel'))
	print(str1.endswith('d'))
	print(str1.endswith('@'))
	print(str1.center(50,'*'))
	print(str1.center(50, ' '))
	print(str1.rjust(50, ' '))

	str2 = 'abc123456'
	print(str2[2])
	print(str2[2:5])
	print(str2[2:])
	print(str2[2::2])
	print(str2[::2])
	print(str2[::-1])
	print(str2[-3:-1])

	print(str2.isdigit())
	print(str2.isalpha())
	print(str2.isalnum())

	str3 = '  jackfrue#@234.com  '
	print(str3)
	print(str3.strip())

if __name__ == '__main__':
	main()

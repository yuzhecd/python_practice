#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 21:14:59
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

def get_suffix(filename, has_dot=False):
	"""
	get the suffix of filename
	"""
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pos + 1
		return filename[index:]
	else:
		return ''

if __name__ == '__main__':
	filename = str(input('Please input a filename: \n'))
	suffix = get_suffix(filename)
	print('The suffix of filename is {}'.format(suffix))

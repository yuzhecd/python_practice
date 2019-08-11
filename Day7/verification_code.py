#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-03 21:03:40
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import random

def generate_code(code_len=4):
	"""
	generate the verifaction code with length 
	of code_len
	"""

	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) - 1
	code = ''

	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]

	return code


if __name__ == '__main__':
	codes = generate_code()
	print(codes)
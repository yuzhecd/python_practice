#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-06-02 21:08:33
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$
import os
import time

def main():
	content = 'welcome to Beijing'
	while True:
		os.system('cls')
		print(content)
		time.sleep(2)
		content = content[1:] + content[0]

if __name__ == '__main__':
	main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 12:20:27
# @Author  : yuzhecd
# @Link    : http://example.org
# @Version : 0.1

year = int(input('请输入年份： '))

is_leap = (year % 4 == 0 and year % 100 != 0 or \
	year % 400 == 0)
print(is_leap)

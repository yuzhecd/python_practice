#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 12:42:21
# @Author  : yuzhecd
# @Link    : http://example.org
# @Version : 0.1

x = float(input('x = '))
if x > 1:
	y = 3 * x - 5
elif x >= -1:
	y = x + 2
else:
	y = 5 * x + 3
print('f(%.2f) = %.2f' % (x, y))

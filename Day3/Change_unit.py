#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 19:27:02
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

value = float(input('请输入长度： '))
unit = input('请输入单位： ')
if unit == 'in' or unit == '英寸':
	print('%f英寸 == %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
	print('%f厘米 == %f英寸' % (value, value / 2.54))
else:
	print('请输入有效的单位')	


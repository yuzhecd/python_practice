#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 19:46:46
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

score = float(input('请输入成绩： '))

if score >= 90:
	grade = 'A'
elif score >= 80:
	grade = 'B'
elif score >= 70:
	grade = 'C'
elif score >= 60:
	grade = 'D'
else:
	grade = 'E'

print('等级：', grade)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 12:04:05
# @Author  : yuzhecd
# @Link    : http://example.org
# @Version : 0.1

f = float(input('请输入华氏温度： '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %1.f摄氏度' % (f, c))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 12:15:04
# @Author  : yuzhecd
# @Link    : http://example.org
# @Version : 0.1

import math

radius = float(input("请输入圆的半径： "))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print('周长： %.2f' % perimeter)
print('面积： %.2f' % area)

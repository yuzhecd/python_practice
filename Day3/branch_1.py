#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 12:34:32
# @Author  : yuzhecd
# @Link    : http://example.org
# @Version : 0.1

username = (input('请输入用户名： '))
password = (input('请输入口令： '))

if username == 'admin' and password == '123456':
	print('身份验证成功')
else:
	print('身份验证失败')

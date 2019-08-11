#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 20:42:58
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import pygame

def main():
	# init the modules of pygame
	pygame.init()
	# init the size of window displayed
	screen = pygame.display.set_mode((800, 600))
	# set the headline of window
	pygame.display.set_caption('big ball eat small ball')
	running = True
	# start an event loop for handling events
	while running:
		# get even from message queue and handle it
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()

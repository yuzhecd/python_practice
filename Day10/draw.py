#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 20:53:25
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import pygame

def main():
	# init the module of pygame
	pygame.init()
	# init the size of window displayed
	screen = pygame.display.set_mode((800, 600))
	# init the headline of window
	pygame.display.set_caption('big ball eat small ball')
	# set the background color of window
	screen.fill((125, 242, 242))
	# draw a circle(window, color, position of center, radius , hollow or not)
	pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
	# flip this window to display pattern
	pygame.display.flip()
	running = True
	# start an even loop to handle envet
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


if __name__ == '__main__':
	main()

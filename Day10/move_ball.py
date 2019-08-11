#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 21:18:56
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('big ball eat small ball')

	x, y = 50, 50
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		screen.fill((255, 255, 255))
		pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)
		pygame.display.flip()
		# every 50ms change the position of ball
		pygame.time.delay(50)
		x, y = x + 5, y + 5

if __name__ == '__main__':
	main()

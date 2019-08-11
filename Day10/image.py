#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 21:10:14
# @Author  : yuzhecd (yuzhecd@163.com)
# @Link    : --------
# @Version : $Id$

import pygame

def main():
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('big ball eat small ball')
	screen.fill((255, 255, 255))
	# import an image
	ball_image = pygame.image.load('./ball.jpg')
	# render on window
	screen.blit(ball_image, (0, 0))
	pygame.display.flip()
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()


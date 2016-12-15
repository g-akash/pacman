#!/usr/bin/env python

import basicSprite
import pygame
from pygame.locals import *

class Snake(basicSprite.Sprite):
	def __init__(self,centerPoint,image):
		basicSprite.Sprite.__init__(self,centerPoint,image)
		self.pellets = 0
		self.x_dist = 3
		self.y_dist = 3

		self.xmove = 0
		self.ymove = 0

	def MoveKeyDown(self, key):
		if key == K_RIGHT:
			self.xmove+=self.x_dist
		elif key == K_LEFT:
			self.xmove-=self.x_dist
		elif key == K_UP:
			self.ymove-=self.y_dist
		elif key == K_DOWN:
			self.ymove+=self.y_dist


	def MoveKeyUp(self,key):
		if key == K_RIGHT:
			self.xmove -= self.x_dist
		elif key == K_LEFT:
			self.xmove+=self.x_dist
		elif key == K_UP:
			self.ymove+=self.y_dist
		elif key == K_DOWN:
			self.ymove-=self.y_dist

	def update(self, block_group):
		self.rect.move_ip(self.xmove,self.ymove)
		if pygame.sprite.spritecollide(self,block_group,False):
			self.rect.move_ip(-self.xmove,-self.ymove)

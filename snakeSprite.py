#!/usr/bin/env python

import basicSprite
import pygame
from pygame.locals import *

SUPER_STATE_START = pygame.USEREVENT + 1
SUPER_STATE_OVER = SUPER_STATE_START + 1
SNAKE_EATEN = SUPER_STATE_OVER + 1

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


	def MonsterCollide(self,lstMonster):
		if len(lstMonster)<=0:
			return
		for monster in lstMonster:
			if monster.scared:
				monster.eaten()
			else:
				pygame.event.post(pygame.event.Event(SNAKE_EATEN,{}))


	def update(self, block_group,pellet_group,super_pellet_group,monstor_group):
		if self.xmove==0 and self.ymove==0:
			return

		self.rect.move_ip(self.xmove,self.ymove)
		

		if pygame.sprite.spritecollide(self,block_group,False):
			self.rect.move_ip(-self.xmove,-self.ymove)

		lst_monstor = pygame.sprite.spritecollide(self,monstor_group,False)
		if len(lst_monstor)>0:
			self.MonsterCollide(lst_monstor)
		else:
			lstcols = pygame.sprite.spritecollide(self,pellet_group, True)
			if len(lstcols)>0:
				self.pellets+=len(lstcols)
			elif (len(pygame.sprite.spritecollide(self, super_pellet_group, True))>0):
				self.superState = True
				pygame.event.post(pygame.event.Event(SUPER_STATE_START,{}))
				pygame.time.set_timer(SUPER_STATE_OVER,0)
				pygame.time.set_timer(SUPER_STATE_OVER,3000)



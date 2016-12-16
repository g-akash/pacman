#!/usr/bin/env python


import basicSprite
import random
import pygame

class Monster(basicSprite.Sprite):
	def __init__(self,centerPoint,image,scared_image = None):
		basicSprite.Sprite.__init__(self,centerPoint,image)
		self.original_rect = pygame.Rect(self)
		self.normal_image = image
		if scared_image != None:
			self.scared_image = scared_image
		else:
			self.scared_image = image
		self.scared = False
		self.direction = random.randint(1,4)
		self.dist = 1
		self.moves = random.randint(100,200)
		self.moveCount = 0

	def update(self,block_group,snake_group):
		xmove,ymove = 0,0
		if self.direction == 1:
			xmove-=self.dist
		elif self.direction == 2:
			ymove-=self.dist
		elif self.direction == 3:
			xmove+=self.dist
		elif self.direction == 4:
			ymove+=self.dist

		self.rect.move_ip(xmove,ymove)
		self.moveCount+=1
		if pygame.sprite.spritecollideany(self,block_group):
			self.rect.move_ip(-xmove,-ymove)
			self.direction = random.randint(1,4)
			self.moves = random.randint(100,200)
			self.moveCount = 0
		elif self.moves == self.moveCount:
			self.direction = random.randint(1,4)
			self.moves = random.randint(100,200)
			self.moveCount = 0
		lst_snake = pygame.sprite.spritecollide(self,snake_group,False)
		if len(lst_snake)>0:
			lst_snake[0].MonsterCollide([self])

	def eaten(self):
		self.rect = self.original_rect
		self.scared = False
		self.image = self.normal_image


	def setScared(self,scared):
		if self.scared != scared:
			self.scared=scared
			if self.scared:
				self.image = self.scared_image
			else:
				self.image = self.normal_image
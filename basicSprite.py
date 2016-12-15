#!/usr/bin/env python

import pygame
from helper import *

class Sprite(pygame.sprite.Sprite):
	def __init__(self,centerPoint,image):
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = image.get_rect()
		self.rect.center = centerPoint


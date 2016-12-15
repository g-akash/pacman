import os,sys
import pygame
from pygame.locals import *

def load_image(name, color_key=None):
	fullname=name
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'cannot load image: ',fullname
		raise SystemExit,message
	image = image.convert()
	if color_key is not None:
		if color_key == -1:
			color_key = image.get_at((0,0))
			image.set_colorkey(color_key,RLEACCEL)
	return image,image.get_rect()

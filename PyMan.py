import os,sys
import pygame
from pygame.locals import *

from helper import *

if not pygame.font: print 'Warning! fonts disable'
if not pygame.mixer: print 'Warning! sounds disabled'


class PyManMain:
	'''The Main Pyman Class - This class handles the main initialization and creating of the Game.'''
	def __init__(self,width=640,height=480):
		'''initialize'''
		'''initialize pygame'''
		pygame.init()
		self.width=width
		self.height=height
		self.screen = pygame.display.set_mode((self.width,self.height))


	def LoadSprites(self):
		'''Load the sprites that we need'''
		self.snake = Snake()
		self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
		numHorizontal = int(self.width/64)
		numVertical = int(self.height/64)
		self.pellet_sprites = pygame.sprite.Group()
		for x in range(numHorizontal):
			for y in range(numVertical):
				self.pellet_sprites.add(Pellet(pygame.Rect(x*64,y*64,64,64)))

	def MainLoop(self):
		'''This is the main loop of the game'''
		self.LoadSprites()
		pygame.key.set_repeat(500,30)
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0,0,0))
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN):
						self.snake.move(event.key)
			lstcols = pygame.sprite.spritecollide(self.snake,self.pellet_sprites,True)
			self.snake.pellets = self.snake.pellets+len(lstcols)
			self.screen.blit(self.background,(0,0))
			if pygame.font:
				font = pygame.font.Font(None,36)
				text = font.render("Pellets %s"%self.snake.pellets,1,(255,0,0))
				textpos = text.get_rect(centerx = self.width/2)
				self.screen.blit(text,textpos)
			self.pellet_sprites.draw(self.screen)
			self.snake_sprites.draw(self.screen)
			pygame.display.flip()


class Snake(pygame.sprite.Sprite):
	'''This is our snake that wll move around'''
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image,self.rect = load_image('./images/snake.png',-1)
		self.pellets = 0
		self.x_dist = 5
		self.y_dist = 5

	def move(self,key):
		'''Move the snake in on of the four directions'''
		xMove = 0
		yMove = 0
		if key == K_RIGHT:
			xMove = self.x_dist
		elif key == K_LEFT:
			xMove = - self.x_dist
		elif key == K_UP:
			yMove = -self.y_dist
		elif key == K_DOWN:
			yMove = self.y_dist
		self.rect.move_ip(xMove,yMove)

class Pellet(pygame.sprite.Sprite):
	def __init__(self,rect=None):
		pygame.sprite.Sprite.__init__(self)
		self.image,self.rect = load_image('./images/pellet.png',-1)
		if rect !=None:
			self.rect = rect

if __name__ == "__main__":
	MainWindow = PyManMain()
	MainWindow.MainLoop()
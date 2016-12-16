import os,sys
import pygame
import level001
import basicSprite
from snakeSprite import *
from pygame.locals import *
from basicMonster import Monster

from helper import *

if not pygame.font: print 'Warning! fonts disable'
if not pygame.mixer: print 'Warning! sounds disabled'


BLOCK_SIZE = 24
counnt=0
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
		x_offset = BLOCK_SIZE/2
		y_offset = BLOCK_SIZE/2

		level1 = level001.level()
		layout = level1.getLayout()
		img_list = level1.getImages()
		self.pellet_sprites = pygame.sprite.RenderUpdates()
		self.block_sprites = pygame.sprite.RenderUpdates()
		self.super_pellet_sprites = pygame.sprite.RenderUpdates()
		self.monster_sprites = pygame.sprite.RenderUpdates()

		for y in range(len(layout)):
			for x in range(len(layout[y])):
				centerPoint = [(x*BLOCK_SIZE)+x_offset,(y*BLOCK_SIZE)+y_offset]
				
				if layout[y][x]==level1.block:
					block = basicSprite.Sprite(centerPoint,img_list[level1.block])
					self.block_sprites.add(block)
				elif layout[y][x] == level1.pellet:
					pellet = basicSprite.Sprite(centerPoint,img_list[level1.pellet])
					self.pellet_sprites.add(pellet)
				elif layout[y][x] == level1.snake:
					self.snake = Snake(centerPoint,img_list[level1.snake])
				elif layout[y][x] == level1.monster:
					monster = Monster(centerPoint,img_list[level1.monster],img_list[level1.scared_monster])
					self.monster_sprites.add(monster)
				elif layout[y][x] == level1.super_pellet:
					super_pellet = basicSprite.Sprite(centerPoint,img_list[level1.super_pellet])
					self.super_pellet_sprites.add(super_pellet)
		self.snake_sprites = pygame.sprite.RenderUpdates((self.snake))


	def MainLoop(self):
		'''This is the main loop of the game'''
		self.LoadSprites()
		self.background = pygame.Surface(self.screen.get_size())
		self.background = self.background.convert()
		self.background.fill((0,0,0))
		self.block_sprites.draw(self.screen)
		self.block_sprites.draw(self.background)
		pygame.display.flip()
		while 1:
			self.snake_sprites.clear(self.screen,self.background)
			self.monster_sprites.clear(self.screen,self.background)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:

					if event.key == K_RIGHT or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN):
						self.snake.MoveKeyDown(event.key)
				elif event.type == KEYUP:
					if event.key == K_RIGHT or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN):
						self.snake.MoveKeyUp(event.key)
				elif event.type == SUPER_STATE_OVER:
					self.snake.superState = False
					pygame.time.set_timer(SUPER_STATE_OVER,0)
					for monster in self.monster_sprites.sprites():
						monster.setScared(False)

				elif event.type == SUPER_STATE_START:
					for monster in self.monster_sprites:
						monster.setScared(True)
				elif event.type == SNAKE_EATEN:
					sys.exit()

			self.snake_sprites.update(self.block_sprites,self.pellet_sprites,self.super_pellet_sprites,self.monster_sprites)
			self.monster_sprites.update(self.block_sprites)
			testpos = 0

			self.screen.blit(self.background,(0,0))
			if pygame.font:
				font = pygame.font.Font(None,36)
				text = font.render("Pellets %s"%self.snake.pellets,1,(255,0,0))
				textpos = text.get_rect(centerx = self.width/2)
				self.screen.blit(text,textpos)

			reclist = [textpos]

			reclist+=self.super_pellet_sprites.draw(self.screen)
			reclist+=self.pellet_sprites.draw(self.screen)
			reclist+=self.snake_sprites.draw(self.screen)
			reclist+=self.monster_sprites.draw(self.screen)

			pygame.display.update(reclist)
			#pygame.display.flip()


# class Snake(pygame.sprite.Sprite):
# 	'''This is our snake that wll move around'''
# 	def __init__(self):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image,self.rect = load_image('./images/snake.png',-1)
# 		self.pellets = 0
# 		self.x_dist = 5
# 		self.y_dist = 5

# 	def move(self,key):
# 		'''Move the snake in on of the four directions'''
# 		xMove = 0
# 		yMove = 0
# 		if key == K_RIGHT:
# 			xMove = self.x_dist
# 		elif key == K_LEFT:
# 			xMove = - self.x_dist
# 		elif key == K_UP:
# 			yMove = -self.y_dist
# 		elif key == K_DOWN:
# 			yMove = self.y_dist
# 		self.rect.move_ip(xMove,yMove)

# class Pellet(pygame.sprite.Sprite):
# 	def __init__(self,rect=None):
# 		pygame.sprite.Sprite.__init__(self)
# 		self.image,self.rect = load_image('./images/pellet.png',-1)
# 		if rect !=None:
# 			self.rect = rect

if __name__ == "__main__":
	MainWindow = PyManMain(500,575)
	MainWindow.MainLoop()
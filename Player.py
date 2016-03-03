import pygame, sys
from pygame.locals import *
from time import *

class Player:

	def __init__(self, name, image, position):
		self.name = name
		self.sprite = pygame.image.load(image)
		self.position = position
		self.facing = 'UP'

import pygame, sys
from pygame.locals import *


# Constants representing different resources
GRASS     = 0
MOUNTAIN1 = 1
MOUNTAIN2 = 2
TEMPLE00  = 3
TEMPLE01  = 4
TEMPLE02  = 5
TEMPLE10  = 6
TEMPLE11  = 7
TEMPLE12  = 8
TEMPLE20  = 9
TEMPLE21  = 10
TEMPLE22  = 11
TREE      = 12
LEDGE1    = 13
LEDGE2    = 14
LEDGE3    = 15
HUT       = 16

# Dictionary linking resources to textures
textures = {
             GRASS     : pygame.image.load('grass.png'),
             MOUNTAIN1 : pygame.image.load('mountain1.png'),
             MOUNTAIN2 : pygame.image.load('mountain2.png'),
             TEMPLE00  : pygame.image.load('temple00.png'),
             TEMPLE01  : pygame.image.load('temple01.png'),
             TEMPLE02  : pygame.image.load('temple02.png'),
             TEMPLE10  : pygame.image.load('temple10.png'),
             TEMPLE11  : pygame.image.load('temple11.png'),
             TEMPLE12  : pygame.image.load('temple12.png'),
             TEMPLE20  : pygame.image.load('temple20.png'),
             TEMPLE21  : pygame.image.load('temple21.png'),
             TEMPLE22  : pygame.image.load('temple22.png'),
             TREE      : pygame.image.load('tree.png'),
             LEDGE1    : pygame.image.load('ledge1.png'),
             LEDGE2    : pygame.image.load('ledge2.png'),
             LEDGE3    : pygame.image.load('ledge3.png'),
	     HUT       : pygame.image.load('hut.png')
           }

# Tilemap
tilemap = [
            [MOUNTAIN1, MOUNTAIN2, TEMPLE00, TEMPLE01, TEMPLE02, GRASS, GRASS, TREE,  GRASS, MOUNTAIN1, MOUNTAIN2],
            [GRASS,     GRASS,     TEMPLE10, TEMPLE11, TEMPLE12, GRASS, GRASS, GRASS, GRASS, GRASS,     MOUNTAIN1],
            [GRASS,     GRASS,     TEMPLE20, TEMPLE21, TEMPLE22, GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ], 
            [GRASS,     GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ],
            [GRASS,     GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ],
            [GRASS,     GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ],
            [GRASS,     GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ],
            [LEDGE1,    GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     GRASS    ],
            [LEDGE2,    GRASS,     GRASS,    GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, TREE,      GRASS    ],
            [LEDGE3,    GRASS,     TREE,     GRASS,    GRASS,    GRASS, GRASS, GRASS, GRASS, GRASS,     HUT      ]
          ]
# Game Dimensions
TILESIZE = 32
MAPWIDTH = 11
MAPHEIGHT = 10

# Initialize Player and Position
PLAYER = pygame.image.load('lyn.png')
playerPos = [MAPWIDTH-1,MAPHEIGHT-1]

# Set up the Display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

while True:

	# Get all user events
	for event in pygame.event.get():
		# If user wants to quit, end game and and close window
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			if (event.key == K_RIGHT) and (playerPos[0] < MAPWIDTH - 1):
				playerPos[0] += 1
			if (event.key == K_LEFT) and (playerPos[0] > 0):
				playerPos[0] -= 1
			if (event.key == K_UP) and (playerPos[1] > 0):
				playerPos[1] -= 1
			if (event.key == K_DOWN) and (playerPos[1] < MAPHEIGHT - 1):
				playerPos[1] += 1

	# Loop through each row
	for row in range(MAPHEIGHT):
		# Loop through each column in the row
		for column in range(MAPWIDTH):
		# Draw the resource at that position in the tilemap
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

	# Display player at current position
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

  	# Up date display
	pygame.display.update()

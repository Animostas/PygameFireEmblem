import pygame, sys
from pygame.locals import *
from time import *

# Turn Debug mode on and off
DEBUG = True

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

WHITE 	  = (255, 255, 255)
BLACK     = (0,   0,   0  )

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
new_coord = []
move_speed = 1.0
move_cd = 4
walk_delay = 1
walk_cd = 0

clock = pygame.time.Clock()

# Set up the Display
pygame.init()
if DEBUG:
	const = 200
	INVFONT = pygame.font.SysFont('FreeSans.tff',18)
	
else:
	const = 0

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+const))

while True:

	# Movment Cooldown Clock
	delta = clock.tick() / 1000.0
	walk_cd -= delta

	if walk_cd <= 0:
		walk_cd = 0

	# Get all user events
	for event in pygame.event.get():
		# If user wants to quit, end game and and close window
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()
		elif (event.type == KEYDOWN):
			if (event.key == K_RIGHT) and (playerPos[0] < MAPWIDTH - 1):
				playerPos[0] += 1
			if (event.key == K_LEFT) and (playerPos[0] > 0):
				playerPos[0] -= 1
			if (event.key == K_UP) and (playerPos[1] > 0):
				playerPos[1] -= 1
			if (event.key == K_DOWN) and (playerPos[1] < MAPHEIGHT - 1):
				playerPos[1] += 1

		elif pygame.mouse.get_pressed()[2]: 
			new_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
			if walk_cd <= 0:
				while new_coord[1] != playerPos[1]:
					if new_coord[1] > playerPos[1]:
						playerPos[1] += 1
						walk_cd = walk_delay
					else:
						playerPos[1] -= 1
						walk_cd = walk_delay
				while new_coord[0] != playerPos[0]:
					if new_coord[0] > playerPos[0]:
						playerPos[0] += 1
						walk_cd = walk_delay
					else:
						playerPos[0] -= 1
						walk_cd = walk_delay

	# Loop through each row
	for row in range(MAPHEIGHT):
		# Loop through each column in the row
		for column in range(MAPWIDTH):
		# Draw the resource at that position in the tilemap
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

	# Display player at current position
	DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))

	# Display DEBUG Information
	if DEBUG:
		placePosition = 5
		Text_Char_Pos = INVFONT.render('Character Position: ' + str(playerPos) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Char_Pos,(placePosition,MAPHEIGHT*TILESIZE))

		cursor_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
		Text_Cursor_Pos = INVFONT.render('Cursor Position: ' + str(cursor_coord) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Cursor_Pos,(placePosition,MAPHEIGHT*TILESIZE+15))

		Text_Button_Statuses = INVFONT.render('Mouse Buttons: ' + str(pygame.mouse.get_pressed()) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Button_Statuses,(placePosition,MAPHEIGHT*TILESIZE+30))

		Text_New_Coords = INVFONT.render('New Coordinates: ' + str(new_coord) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_New_Coords,(placePosition, MAPHEIGHT*TILESIZE + 46))

		Text_Walk_Cooldown = INVFONT.render('Movement Cooldown: ' + str(walk_cd) + (9*'       '), True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Walk_Cooldown,(placePosition + 175, MAPHEIGHT*TILESIZE))
	pygame.display.update()

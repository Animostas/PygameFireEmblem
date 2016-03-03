import pygame, sys

# Constants representing different resouces
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

terrains =  {
		0  : 'GRASS',
		1  : 'MOUNTAIN1',
		2  : 'MOUNTAIN2',
		3  : 'TEMPLE00',
		4  : 'TEMPLE01',
		5  : 'TEMPLE02',
		6  : 'TEMPLE10',
		7  : 'TEMPLE11',
		8  : 'TEMPLE12',
		9  : 'TEMPLE20',
		10 : 'TEMPLE21',
		11 : 'TEMPLE22',
		12 : 'TREE',
		13 : 'LEDGE1',
		14 : 'LEDGE2',
		15 : 'LEDGE3',
		16 : 'HUT'
	     }

# Dictionary linking resouces to textures
textures = {
             GRASS     : pygame.image.load('Textures/grass.png'),
             MOUNTAIN1 : pygame.image.load('Textures/mountain1.png'),
             MOUNTAIN2 : pygame.image.load('Textures/mountain2.png'),
             TEMPLE00  : pygame.image.load('Textures/temple00.png'),
             TEMPLE01  : pygame.image.load('Textures/temple01.png'),
             TEMPLE02  : pygame.image.load('Textures/temple02.png'),
             TEMPLE10  : pygame.image.load('Textures/temple10.png'),
             TEMPLE11  : pygame.image.load('Textures/temple11.png'),
             TEMPLE12  : pygame.image.load('Textures/temple12.png'),
             TEMPLE20  : pygame.image.load('Textures/temple20.png'),
             TEMPLE21  : pygame.image.load('Textures/temple21.png'),
             TEMPLE22  : pygame.image.load('Textures/temple22.png'),
             TREE      : pygame.image.load('Textures/tree.png'),
             LEDGE1    : pygame.image.load('Textures/ledge1.png'),
             LEDGE2    : pygame.image.load('Textures/ledge2.png'),
             LEDGE3    : pygame.image.load('Textures/ledge3.png'),
	     HUT       : pygame.image.load('Textures/hut.png')
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

# Walls
PASSABLE     = [MOUNTAIN1, MOUNTAIN2, GRASS, TREE, HUT, TEMPLE21]
NOT_PASSABLE = [LEDGE1, LEDGE2, LEDGE3, TEMPLE00, TEMPLE01, TEMPLE02, TEMPLE10, TEMPLE11, TEMPLE12, TEMPLE20, TEMPLE21, TEMPLE22]

# Game Dimensions
TILESIZE = 32
MAPWIDTH = 11
MAPHEIGHT = 10

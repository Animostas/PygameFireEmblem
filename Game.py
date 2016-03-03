import pygame, sys
from pygame.locals import *
from time import *
from SacaeMap import *
from Player import *

# Turn Debug mode on and off
DEBUG = True

# Information for Error Handling
WHITE = [255, 255, 255]
BLACK = [0  , 0  , 0  ]
RED   = [255, 0, 0]
case  = 0

# Initialize Players and Positions
Lord   = Player('Lord',   'CharacterSprites/lyn.png',    [10,9])
Mage   = Player('Mage',   'CharacterSprites/mage.png',   [9,9])
Archer = Player('Archer', 'CharacterSprites/archer.png', [8,9])
Bard   = Player('Bard',   'CharacterSprites/bard.png',   [7,9])

listPLAYERS = [Lord, Mage, Archer, Bard]

walk_delay = 1
walk_cd = 0

HOTKEYS = {
		1 : Lord, 
		2 : Mage, 
		3 : Archer, 
		4 : Bard
	  }

# First player is default
PLAYER = listPLAYERS[0]
PLAYER_NAME = listPLAYERS[0].name
playerPos = listPLAYERS[0].position
new_coord = playerPos
clock = pygame.time.Clock()
facing = listPLAYERS[0].facing

# Initialize Cursor to load on Default Character
Cursor = pygame.image.load('CharacterSprites/cursor.png')
cursorPos = PLAYER.position

# Set up the Display
pygame.init()
if DEBUG:
	const = 200
	INVFONT = pygame.font.SysFont('FreeSans.tff',18)
	
else:
	const = 0

DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+const))

while True:

	mouse_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
	cursorPos = PLAYER.position

	# Movement Cooldown Clock
	turn_clock = clock.tick() / 1000.0
	walk_cd -= turn_clock

	# Get all user events
	for event in pygame.event.get():
		# If user wants to quit, end game and and close window
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()

		# Mouse inputs
		elif pygame.mouse.get_pressed()[0]:
			for player in listPLAYERS:
				if player.position == mouse_coord:
					PLAYER = player

		elif pygame.mouse.get_pressed()[2]: 
			new_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
			case = 0
			for player in listPLAYERS:
				if player != PLAYER:
					if new_coord == player.position:
						case = 3
			if tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
				case = 2
			elif PLAYER.move_current_cd > 0:
				case = 4
			elif (PLAYER.move_current_cd <= 0) and (case == 0):
				for i in range(len(new_coord)):
					while PLAYER.position[i] != new_coord[i]:
						if new_coord[i] > PLAYER.position[i]:
							PLAYER.position[i] += 1
						if new_coord[i] < PLAYER.position[i]:
							PLAYER.position[i] -= 1

		elif (event.type == KEYDOWN):
			# Keyboard Inputs
			if (event.key == K_RIGHT):
				PLAYER.facing = 'RIGHT'
				increment = 1
				case = 0
				new_coord = [PLAYER.position[0]+1, PLAYER.position[1]]
				if new_coord[0] not in range(MAPWIDTH):
					increment = 0
					case = 1
				elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
					increment = 0
					case = 2
				else:
					for player in listPLAYERS:
						if new_coord == player.position:
							increment = 0
							case = 3
				PLAYER.position[0] += increment

			if (event.key == K_LEFT):
				PLAYER.facing = 'LEFT'
				increment = 1
				case = 0
				new_coord = [PLAYER.position[0]-1, PLAYER.position[1]]
				if new_coord[0] not in range(MAPWIDTH):
					increment = 0
					case = 1
				elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
					increment = 0
					case = 2
				else:
					for player in listPLAYERS:
						if new_coord == player.position:
							increment = 0
							case = 3
				PLAYER.position[0] -= increment

			if (event.key == K_UP):
				PLAYER.facing = 'UP'
				increment = 1
				case = 0
				new_coord = [PLAYER.position[0], PLAYER.position[1]-1]
				if new_coord[1] not in range(MAPHEIGHT):
					increment = 0
					case = 1
				elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
					increment = 0
					case = 2
				else:
					for player in listPLAYERS:
						if new_coord == player.position:
							increment = 0
							case = 3
				PLAYER.position[1] -= increment

			if (event.key == K_DOWN):
				PLAYER.facing = 'DOWN'
				increment = 1
				case = 0
				new_coord = [PLAYER.position[0], PLAYER.position[1]+1]
				if new_coord[1] not in range(MAPHEIGHT):
					increment = 0
					case = 1
				elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
					increment = 0
					case = 2
				else:
					for player in listPLAYERS:
						if new_coord == player.position:
							increment = 0
							case = 3
				PLAYER.position[1] += increment

			# Mapping Hotkeys
			if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
				if (event.key == K_1):
					HOTKEYS[1] = PLAYER
				if (event.key == K_2):
					HOTKEYS[2] = PLAYER
				if (event.key == K_3):
					HOTKEYS[3] = PLAYER
				if (event.key == K_4):
					HOTKEYS[4] = PLAYER

			# Hotkeys to switch between units
			else:
				if (event.key == K_1):
					PLAYER = HOTKEYS[1]
					cursorPos = PLAYER.position
					new_coord = cursorPos
				if (event.key == K_2):
					PLAYER = HOTKEYS[2]
					cursorPos = PLAYER.position
					new_coord = cursorPos
				if (event.key == K_3):
					PLAYER = HOTKEYS[3]
					cursorPos = PLAYER.position
					new_coord = cursorPos
				if (event.key == K_4):
					PLAYER = HOTKEYS[4]
					cursorPos = PLAYER.position
					new_coord = cursorPos

	# Display map sprites
	for row in range(MAPHEIGHT):
		for column in range(MAPWIDTH):
			DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE))

	# Display players and cursor
	DISPLAYSURF.blit(Cursor,(cursorPos[0]*TILESIZE,cursorPos[1]*TILESIZE))
	for player in listPLAYERS:
		DISPLAYSURF.blit(player.sprite,(player.position[0]*TILESIZE,player.position[1]*TILESIZE))

	# Display DEBUG Information
	if DEBUG:
		placePosition = 5
		Text_Char_Pos = INVFONT.render('Character Position: {}'.format(PLAYER.position) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Char_Pos,(placePosition,MAPHEIGHT*TILESIZE))

		mouse_coord = [pygame.mouse.get_pos()[0]/TILESIZE, pygame.mouse.get_pos()[1]/TILESIZE]
		Text_Mouse_Pos = INVFONT.render('Cursor Position: ' + str(mouse_coord) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Mouse_Pos,(placePosition,MAPHEIGHT*TILESIZE+15))

		Text_Button_Facing = INVFONT.render('Direction Facing: ' + str(PLAYER.facing) + 9 * '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Button_Facing,(placePosition,MAPHEIGHT*TILESIZE+30))

		Text_New_Coords = INVFONT.render('Desired Coordinates: ' + str(new_coord) + '  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_New_Coords,(placePosition, MAPHEIGHT*TILESIZE+45))

		error_cases = {
				1 : 'OUT OF BOUNDS',
				2 : 'IMPASSABLE TERRAIN',
				3 : 'CHARACTER OCCUPYING TILE',
				4 : 'MOVEMENT COOLDOWN'
			      }
		Text_Valid = INVFONT.render(1000 * ' ', True, BLACK, BLACK)
		if case != 0:
			Text_Valid = INVFONT.render('INVALID COMMAND: {}'.format(error_cases[case]) + 10*'   ', True, RED, BLACK)
		DISPLAYSURF.blit(Text_Valid,(placePosition, MAPHEIGHT*TILESIZE+60))
			
		Text_Char_Selected = INVFONT.render('Currently Selected: ' + PLAYER.name + '        ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Char_Selected,(placePosition, MAPHEIGHT*TILESIZE+75))

		Text_Hotkey1 = INVFONT.render('1 : {}'.format(HOTKEYS[1].name) + 5*'  ', True, WHITE, BLACK)
		Text_Hotkey2 = INVFONT.render('2 : {}'.format(HOTKEYS[2].name) + 5*'  ', True, WHITE, BLACK)
		Text_Hotkey3 = INVFONT.render('3 : {}'.format(HOTKEYS[3].name) + 5*'  ', True, WHITE, BLACK)
		Text_Hotkey4 = INVFONT.render('4 : {}'.format(HOTKEYS[4].name) + 5*'  ', True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Hotkey1,(placePosition + 200, MAPHEIGHT * TILESIZE))
		DISPLAYSURF.blit(Text_Hotkey2,(placePosition + 200, MAPHEIGHT * TILESIZE + 15))
		DISPLAYSURF.blit(Text_Hotkey3,(placePosition + 200, MAPHEIGHT * TILESIZE + 30))
		DISPLAYSURF.blit(Text_Hotkey4,(placePosition + 200, MAPHEIGHT * TILESIZE + 45))

#		Text_Walk_Cooldown = INVFONT.render('Current Char CD: ' + str(PLAYER.move_current_cd) + (20*' '), True, WHITE, BLACK)
#		DISPLAYSURF.blit(Text_Walk_Cooldown,(placePosition + 175, MAPHEIGHT*TILESIZE))

		current_terrain = terrains[tilemap[PLAYER.position[1]][PLAYER.position[0]]]
		Text_Terrain = INVFONT.render('Terrain: ' + str(current_terrain) + (9*'  '), True, WHITE, BLACK)
		DISPLAYSURF.blit(Text_Terrain,(placePosition, MAPHEIGHT*TILESIZE+90))

	pygame.display.update()

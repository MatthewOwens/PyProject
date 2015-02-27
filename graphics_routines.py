# Pykemon Battle

import random, pygame, sys
from pygame.locals import *
from move import typeString

kScreenWidth = 320
kScreenHeight = 240

#             R    G    B
kColourWhite = (255, 255, 255)
kColourGray = (128, 128, 128)
kColourBlack = (  0,   0,   0)
BackgroundColour = kColourWhite

kTargetFPS = 15

squirtle_sprite = pygame.image.load("sprites/squirtle.png")
bulbasaur_sprite = pygame.image.load("sprites/bulbasaur.png")

def init_graphics():
    global FPSCLOCK, DisplaySurface, DefaultFont

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DisplaySurface = pygame.display.set_mode((kScreenWidth, kScreenHeight))
    DefaultFont = pygame.font.Font('freesansbold.ttf', 16)
    pygame.display.set_caption('Poke Battle!')

def render_begin():
    DisplaySurface.fill(BackgroundColour)
	
def render_end():
    pygame.display.update()
    FPSCLOCK.tick(kTargetFPS)

def drawText(text, pos):
    pressKeySurf = DefaultFont.render(text, True, kColourBlack)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = pos
    DisplaySurface.blit(pressKeySurf, pressKeyRect)

def drawProgressBar(Position, CurrentPercent, Width):
	x, y = Position[0], Position[1]
	pygame.draw.rect(DisplaySurface, kColourBlack, [x, y, Width, 8], 1) # bg
	pygame.draw.rect(DisplaySurface, kColourBlack, [x, y, Width * CurrentPercent, 8], 0) # bg
	
def drawPokeStats(Position, Name, Level, CurrentHp, MaximumHp, CurrentExp, MaximumExp):
	drawText(Name, Position) # Name
	drawText(":L" + str(Level), tuple(map(sum, zip(Position,(43, 15))))) # Level
	drawText("HP:", tuple(map(sum, zip(Position,(0, 30))))) # Hp Text
	drawProgressBar(tuple(map(sum, zip(Position,(35, 35)))), CurrentHp / MaximumHp, 60) # Hp Progress Bar
	drawText(str(CurrentHp) + " / " + str(MaximumHp), tuple(map(sum, zip(Position,(35, 50))))) # Hp Values
	drawProgressBar(tuple(map(sum, zip(Position,(0, 68)))), CurrentExp / MaximumExp, 100) # Exp Bar

def drawActionBox(SelectedColumn, SelectedRow):
	pygame.draw.rect(DisplaySurface, kColourBlack, [160, 164, 160, 75], 2) # action box
	pygame.draw.rect(DisplaySurface, kColourBlack, [165 + 70 * SelectedColumn, 180 + 34 * SelectedRow, 10, 10], 0) # action cursor
	
	drawText("Fight", (180, 176))
	drawText("Pkmn", (250, 176))
	drawText("Item", (180, 210))
	drawText("Run", (250, 210))

def drawMessageBox(Line1, Line2, Line3):
	pygame.draw.rect(DisplaySurface, kColourGray, [0, 164, 319, 75], 2) # messagebox
	drawText(Line1, (5, 175))
	drawText(Line2, (5, 195))
	drawText(Line3, (5, 215))
	
def drawMoveMenu(SelectedIndex, MovesList):
	pygame.draw.rect(DisplaySurface, kColourWhite, [15, 114, 150, 50], 0) # white bg for text
	pygame.draw.rect(DisplaySurface, kColourGray, [15, 114, 150, 50], 1) # box
	drawText("TYPE /", (20, 125))
	#drawText("NORMAL", (20, 145))
	drawText(typeString(MovesList[SelectedIndex].Type), (20, 145))
	#drawText("35 / 35", (100, 145))
	drawText(str(MovesList[SelectedIndex].currentPP) + " / " + str(MovesList[SelectedIndex].maxPP), (100, 145))
	pygame.draw.rect(DisplaySurface, kColourBlack, [130, 164, 190, 75], 1) # moves box
	pygame.draw.rect(DisplaySurface, kColourBlack, [135, 175 + 16 * SelectedIndex, 10, 5], 0) # action cursor
	for index in range(0, 4):
		if (index < len(MovesList)):
			drawText(MovesList[index].Name, (145, 170 + index * 16))
		else:
			drawText("-", (145, 170 + index * 16))
	
def drawPokemonSprites():
	DisplaySurface.blit(bulbasaur_sprite, (10, 170))
	DisplaySurface.blit(squirtle_sprite, (215, 5))

def drawBulbasaur():
	DisplaySurface.blit(bulbasaur_sprite, (10, 170))

def drawSquirtle():
	DisplaySurface.blit(squirtle_sprite, (215, 5))

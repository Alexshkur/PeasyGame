import pygame
import math
import os
from pygame.locals import *
import subprocess
pygame.init()
screen = pygame.display.set_mode((50, 50))
pygame.display.set_caption('Creative Drawing Program')
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
GREY = (153, 153, 153)
#Math
PI = 3.14159265358979323846
HALF_PI = 1.57079632679489661923
QUARTER_PI = 0.7853982
TWO_PI = 6.28318530717958647693
def sin(num):
	if isinstance(num, int):
		num = math.sin(num)
	elif isinstance(num, list):
		for i, val in enumerate(num):
			num[i] = math.sin(val)
	else: 
		raise TypeError(f"type {type(num)} in number unsupported")
	return num
def cos(num):
	return math.cos(num)
def constrain(value, minV, maxV):
	if not isinstance(minV, int): 
		raise TypeError(f"type {type(minV)} in min value is unsupported")
	if not isinstance(maxV, int): 
		raise TypeError(f"type {type(maxV)} in max value is unsupported")
	if isinstance(value, int):
		if value > maxV:
			value = maxV
		if value < minV:
			value = minV
	elif isinstance(value, list):
		for i, val in enumerate(value):
			if value[i] > maxV:
				value[i] = maxV
			if value[i] < minV:
				value[i] = minV
	else: 
		raise TypeError(f"type {type(value)} in value is unsupported")
	return value
def mouseIn(x, y, w, h):
	if mouseX > x and mouseX < x+w:
		if mouseY > y and mouseY < y+h:
			return True
		else: return False
	else: return False
#Cosmetics
def setFont(FontPath, size):
	global font
	global fontPath
	global fontSize
	if os.path.exists(FontPath):
		if not os.path.isdir(FontPath):
			font = pygame.font.Font(FontPath, size)
			fontPath = FontPath
			fontSize = size
		else: raise IsADirectoryError("'" + FontPath + "' is a directory!")
	else: raise FileNotFoundError("'" + FontPath + "' is not exists")
def setFontSize(size):
	setFont(getFont(), size)
def getFont(WithSize=False):
	global fontPath
	global fontSize
	if WithSize:
		return fontPath, fontSize
	else:
		return fontPath
def getFill():
	global fillColor
	return fillColor
#System variables/functions
font = ""
fontPath = ""
fontSize = 0
backgroundColor = BLACK
fillColor = BLACK
width = 0
height = 0
frame = 0
AppCenter = (width/2, height/2)
mouseX = 0
mouseY = 0
MousePressed = False
MouseButton = 0
Draws = []
true = True
false = False
def run(command):
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
	while True:
		output = process.stdout.readline()
		if output == '' and process.poll() is not None:
			break
		if output:
			print(output.strip())
	rc = process.poll()
	if rc is not None:
		for output in process.stdout.readlines():
			print(output.strip())
def tick():
	global width
	global height
	global AppCenter
	width, height = screen.get_size()
	AppCenter = (width/2, height/2)
	global PI
	global HALF_PI
	global QUATERTER_PI
	global TWO_PI
	PI = 3.14159265358979323846
	HALF_PI = 1.57079632679489661923
	QUARTER_PI = 0.7853982
	TWO_PI = 6.28318530717958647693
#Color functions
def getRGB(color):
	if isinstance(color, tuple):
		return (constrain(color[0], 0, 255), constrain(color[1], 0, 255), constrain(color[2], 0, 255))
	elif isinstance(color, str):
		if color[0:1] == "#":
			return tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
		else: raise TypeError(f"str {color} is not html-color")
	else: raise TypeError(f"Unpupported type {type(color)}")
def getHTML(color):
	if isinstance(color, tuple):
		return '#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2])
#Fill app
def background(color):
	global backgroundColor
	if isinstance(color, tuple):
		screen.fill(getRGB(color))
		backgroundColor = getRGB(color)
	elif isinstance(color, str):
		if color[0:1] == "#" and len(color) == 7:
			screen.fill(getRGB(color))
			backgroundColor = getRGB(color)
		else: raise TypeError(f"str {color} is not html-color")
	else: raise TypeError(f"Unpupported type {type(color)}")
def fill(color):
	global fillColor
	if isinstance(color, tuple):
		fillColor = getRGB(color)
	elif isinstance(color, str):
		if color[0:1] == "#" and len(color) == 7:
			fillColor = getRGB(color)
		else: raise TypeError(f"str {color} is not html-color")
	else: raise TypeError(f"Unpupported type {type(color)}")
#Circle
def circle(x, y, radius, width=0):
	global fillColor
	pygame.draw.circle(screen, fillColor, (x, y), radius, width)
#Rect
def rect(x, y, w, h, width=0):
	global fillColor
	pygame.draw.rect(screen, fillColor, (x, y, w, h), width)
#line
def line(x, y, x2, y2, width=1):
	global fillColor
	pygame.draw.line(screen, fillColor, (x, y), (x2, y2), width)
#ellipse
def ellipse(x, y, w, h, width=0):
	global fillColor
	pygame.draw.ellipse(screen, fillColor, pygame.Rect(x-w//2, y-h//2, w, h), width)
#text
def text(text, x, y):
	global font
	FontedText = font.render(text, True, fillColor)
	TextRect = FontedText.get_rect(center=(x, y))
	screen.blit(FontedText, TextRect)
#size
def size(w, h, resizable=false):
	if resizable:
		screen = pygame.display.set_mode((w, h), RESIZABLE)
	else:
		screen = pygame.display.set_mode((w, h))
def getScreen():
	return pygame.surfarray.array3d(screen)
def exit():
	global running
	running = False
def addDraw(function):
	global Draws
	Draws.append(function)
running = True
background(GREY)
setup()
pygame.display.flip()
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		elif event.type == MOUSEMOTION:
			mouseX, mouseY = event.pos
			mouseX = constrain(mouseX, 0, width)
			mouseY = constrain(mouseY, 0, height)
			if hasattr(sys.modules[__name__], 'mouseDragged'): mouseDragged()
		elif event.type == VIDEORESIZE:
			background(GREY)
			if hasattr(sys.modules[__name__], 'resized'): resized()
		elif event.type == MOUSEBUTTONDOWN:
			MouseButton = event.button
			MousePressed = True
			if hasattr(sys.modules[__name__], 'mousePressed'): mousePressed()
		elif event.type == MOUSEBUTTONUP:
			MousePressed = False
			if hasattr(sys.modules[__name__], 'mouseReleased'): mouseReleased()
		elif event.type == MOUSEWHEEL:
			if hasattr(sys.modules[__name__], 'mouseWheel'): mouseWheel(event.y)
	tick()
	if hasattr(sys.modules[__name__], 'draw'): draw()
	frame += 1
	for func in Draws:
		func()
	pygame.display.flip()
pygame.quit()
sys.exit()
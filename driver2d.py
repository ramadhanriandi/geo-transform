import transform2d as t2d
import numpy as np
import pygame
from pygame.locals import *

Point = np.empty([100,2], dtype=float)
Point_output = np.empty([100,2], dtype=float)
Start = np.empty([100,2], dtype=float)
Keluar = False

NbPoint = int(input('Banyak titik : '))
t2d.InputPoint(Point, Start, NbPoint)

my_tuple = t2d.ListToTuple(Point, NbPoint)
print(my_tuple)

pygame.init()
#clock = pygame.time.Clock()

window = pygame.display.set_mode((1000,1000))

purple = (155,0,155)
black = (0,0,0)

while not(Keluar) :
	pygame.event.get()
	
	Command = input('Perintah : ').split(' ')
	
	if (Command[0] == 'translate') :
		dx = float(Command[1])
		dy = float(Command[2])
		t2d.Translate(Point, dx, dy, NbPoint)
	elif (Command[0] == 'dilate') :
		k = float(Command[1])
		t2d.Dilate(Point, k, NbPoint)
	elif (Command[0] == 'rotate') :
		deg = float(Command[1])
		a = float(Command[2])
		b = float(Command[3])
		t2d.Rotate(Point, deg, a, b, NbPoint)
	elif (Command[0] == 'reflect') :
		param = Command[1]
		t2d.Reflect(Point, param, NbPoint)
	elif (Command[0] == 'shear') :
		param = Command[1]
		k = float(Command[2])
		t2d.Shear(Point, param, k, NbPoint)
	elif (Command[0] == 'stretch') :
		param = Command[1]
		k = float(Command[2])
		t2d.Stretch(Point, param, k, NbPoint)
	elif (Command[0] == 'custom') :
		a = float(Command[1])
		b = float(Command[2])
		c = float(Command[3])
		d = float(Command[4])
		t2d.Custom(Point, a, b, c, d, NbPoint)
	elif (Command[0] == 'multiple') :
		n = int(Command[1])
		t2d.Multiple(Point, n, NbPoint)
	elif (Command[0] == 'reset') :
		for i in range (NbPoint) :
			Point[i] = Start[i]
	elif (Command[0] == 'exit') :
		Keluar = True
	
	for i in range (NbPoint) :
		Point_output[i][0] = 500 + Point[i][0]
		Point_output[i][1] = 500 - Point[i][1]
	
	my_tuple = t2d.ListToTuple(Point_output, NbPoint)
	#print(my_tuple)
	
	window.fill(black)
	pygame.draw.polygon(window, (purple), my_tuple)
	pygame.draw.line(window, (155,155,155), (0,500), (1000,500), 2)
	pygame.draw.line(window, (155,155,155), (500,0), (500,1000), 2)
	
	pygame.display.update()


import numpy as np
import math

def InputPoint(Point, Start, NbPoint) :
    for i in range (NbPoint) :
        Point[i][0], Point[i][1] = map(float, input('Titik ke-%d : ' %(i+1)).split(','))
        Start[i] = Point[i]

def Translate(Point, dx, dy, NbPoint) :
    for i in range (NbPoint) :
        Point[i][0] += dx
        Point[i][1] += dy
    return Point

def Dilate(Point, k, NbPoint) :
	for i in range (NbPoint) :
		Point[i] *= k
	return Point

def Rotate(Point, deg, a, b, NbPoint) : 
    for i in range (NbPoint) :
        Ptemp1 = Point[i][0]
        Ptemp2 = Point[i][1]
        Point[i][0] = (Ptemp1-a)*math.cos(math.radians(deg)) - (Ptemp2-b)*math.sin(math.radians(deg)) + a
        Point[i][1] = (Ptemp1-a)*math.sin(math.radians(deg)) + (Ptemp2-b)*math.cos(math.radians(deg)) + b
    return Point

def Reflect(Point, param, NbPoint) :
    p = param.split(',')
    if (len(p) == 2) :
        a = float(p[0][1:])
        b = float(p[1][:len(p[1])-1])
        for i in range (NbPoint) :
            Point[i][0] = 2*a - Point[i][0]
            Point[i][1] = 2*b - Point[i][1]
    else :
        if (param == 'x') :
            for i in range (NbPoint) :
                Point[i][1] = -Point[i][1]
        elif (param == 'y') :
            for i in range (NbPoint) :
                Point[i][0] = -Point[i][0]
        elif (param == 'y=x') :
            for i in range (NbPoint) :
                Ptemp = Point[i][0]
                Point[i][0] = Point[i][1]
                Point[i][1] = Ptemp
        elif (param == 'y=-x') :
            for i in range (NbPoint) :
                Ptemp = Point[i][0]
                Point[i][0] = -Point[i][1]
                Point[i][1] = -Ptemp
    return Point

def Shear(Point, param, k, NbPoint) :
    if (param == 'x') :
        for i in range (NbPoint) :
            Point[i][0] += k*Point[i][1]
    elif (param == 'y') :
        for i in range (NbPoint) :
            Point[i][1] += k*Point[i][0]
    return Point

def Stretch(Point, param, k, NbPoint) :
    if (param == 'x') :
        for i in range (NbPoint) :
            Point[i][0] *= k
    elif (param == 'y') :
        for i in range (NbPoint):
            Point[i][1] *= k
    return Point

def Custom (Point, a, b, c, d, NbPoint) :
    for i in range (NbPoint) :
        Ptemp1 = Point[i][0]*a + Point[i][1]*b
        Ptemp2 = Point[i][0]*c + Point[i][1]*d
        Point[i][0] = Ptemp1
        Point[i][1] = Ptemp2
    return Point

def Multiple(Point, n, NbPoint) :
    for i in range(n):
        Command = input('Tahap %d : ' % (i+1)).split(' ')
        if Command[0] == "translate":
            Point = Translate(Point, float(Command[1]), float(Command[2]), NbPoint)
        elif Command[0] == "dilate":
            Point = Dilate(Point, float(Command[1]), NbPoint)
        elif Command[0] == 'rotate':
            Point = Rotate(Point, float(Command[1]), float(Command[2]), float(Command[3]), NbPoint)
        elif Command[0] == 'reflect':
            Point = Reflect(Point, Command[1], NbPoint)
        elif Command[0] == 'shear':
            Point = Shear(Point, Command[1], float(Command[2]), NbPoint)
        elif Command[0] == 'stretch':
            Point = Stretch(Point, Command[1], float(Command[2]), NbPoint)
        elif Command[0] == 'custom':
            Point = Custom(Point, float(Command[1]), float(Command[2]), float(Command[3]), float(Command[4]), NbPoint)
    return Point

def ListToTuple(Point, NbPoint) :
	hasil = list()
	
	for i in range (NbPoint) :
		conversion = tuple(Point[i])
		hasil.append(conversion)		

	return hasil
	
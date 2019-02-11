import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math
from math import *
import transform3d as t3d
import OpenGL
import time
import threading
import sys, math, pygame


global Command
msk = 120.0 
width = 1000 
height = 1000 
rasio = width / height 
horizontal = 0 
vertikal = 0 
rasio = width / height 


def titik(Point):
	Point[0]=(1,-1,-1)
	Point[1]=(1,1,-1)
	Point[2]=(-1,1,-1)
	Point[3]=(-1,-1,-1)
	Point[4]=(1,-1,1)
	Point[5]=(1,1,1)
	Point[6]=(-1,-1,1)
	Point[7]=(-1,1,1)
	return Point

def sisi(Face):
	Face[0]=(0,1,2,3)
	Face[1]=(1,5,6,2)
	Face[2]=(5,4,7,6)
	Face[3]=(4,0,3,7)
	Face[4]=(0,4,5,1)
	Face[5]=(3,2,6,7)
	return Face

def warna(Color):
	Color[0]=(1,1,0,1)
	Color[1]=(1,0,1,1)
	Color[2]=(0,1,1,1)
	Color[3]=(0,1,0,1)
	Color[4]=(1,0,0,1)
	Color[5]=(0,0,1,1)
	return Color

Point = np.empty([100,3], dtype=float)
Start = np.empty([100,3], dtype=float)
titik(Point)
titik(Start)
Face = np.empty([100,4], dtype=float)
sisi(Face)
Color = np.empty([100,4], dtype=float)
warna(Color)

	
def init():
	 
	glClearColor(0,0,0,1)
	glViewport(0, 0, 1000, 1000)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(65, 1000/1000., .1, 1000)
	glMatrixMode(GL_MODELVIEW)
	
	glEnable(GL_DEPTH_TEST)
	
def kubus(Point, Face, Color):
				
		glBegin(GL_QUADS)

		glColor4d(1,1,0,1)
		glVertex3d(Point[3][0],Point[3][1],Point[3][2])
		glVertex3d(Point[0][0],Point[0][1],Point[0][2])
		glVertex3d(Point[1][0],Point[1][1],Point[1][2])
		glVertex3d(Point[2][0],Point[2][1],Point[2][2])
				
		glColor4d(1,0,1,1)
		glVertex3d(Point[6][0],Point[6][1],Point[6][2])
		glVertex3d(Point[4][0],Point[4][1],Point[4][2])
		glVertex3d(Point[5][0],Point[5][1],Point[5][2])
		glVertex3d(Point[7][0],Point[7][1],Point[7][2])
				
		glColor4d(0,1,1,1)
		glVertex3d(Point[3][0],Point[3][1],Point[3][2])
		glVertex3d(Point[2][0],Point[2][1],Point[2][2])
		glVertex3d(Point[7][0],Point[7][1],Point[7][2])
		glVertex3d(Point[6][0],Point[6][1],Point[6][2])
				
		glColor4d(0,1,0,1)
		glVertex3d(Point[0][0],Point[0][1],Point[0][2])
		glVertex3d(Point[1][0],Point[1][1],Point[1][2])
		glVertex3d(Point[5][0],Point[5][1],Point[5][2])
		glVertex3d(Point[4][0],Point[4][1],Point[4][2])
				
		glColor4d(1,0,0,1)
		glVertex3d(Point[3][0],Point[3][1],Point[3][2])
		glVertex3d(Point[0][0],Point[0][1],Point[0][2])
		glVertex3d(Point[4][0],Point[4][1],Point[4][2])
		glVertex3d(Point[6][0],Point[6][1],Point[6][2])
			
		glColor4d(0,0,1,1)
		glVertex3d(Point[2][0],Point[2][1],Point[2][2])
		glVertex3d(Point[1][0],Point[1][1],Point[1][2])
		glVertex3d(Point[5][0],Point[5][1],Point[5][2])
		glVertex3d(Point[7][0],Point[7][1],Point[7][2])

		glEnd()
	
def garis () :
		panjang = 500
		glLineWidth(3)
		glBegin(GL_LINES)

		
		glColor3f(1,0.5,0)
		glVertex3d(0.0,0.0,0.0)
		glVertex3d(-1*panjang,0.0,0.0)
		glVertex3d(panjang,0.0,0.0)

		  
		glVertex3d(0,0,0)
		glVertex3d(0,panjang,0)
		glVertex3d(0,-1*panjang,0)

		
		glVertex3d(0,0,0)
		glVertex3d(0.0,0.0,panjang)

	
		glVertex3d(0,0,0)
		glVertex3d(0.0,0.0,-1.0*panjang)

		glEnd()

def grid ():
		panjang = 500
		glLineWidth(1)
		glBegin(GL_LINES)
			
		glColor4f(0.5,1,1, 0); 

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,0.0,i)
				glVertex3d(panjang,0.0,i)

		for i in range (-1*int(panjang), int(panjang)) :
				glVertex3d(0.0,0.0,i)
				glVertex3d(-1*panjang,0.0,i)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,i,0.0)
				glVertex3d(panjang,i,0.0)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,i,0.0)
				glVertex3d(-1*panjang,i,0.0)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(i,0.0,0.0)
				glVertex3d(i,0.0,panjang)

		for i in range (-1*int(panjang), int(panjang)) :
				glVertex3d(i,0.0,0.0)
				glVertex3d(i,0.0,-1*panjang)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,i,0.0)
				glVertex3d(0.0,i,panjang)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,i,0.0)
				glVertex3d(0.0,i,-1*panjang)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(i,0.0,0.0)
				glVertex3d(i,panjang,0.0)

		for i in range (-1*int(panjang), int(panjang)) :
				glVertex3d(i,0.0,0.0)
				glVertex3d(i,-1*panjang,0.0)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,0.0,i)
				glVertex3d(0.0,panjang,i)

		for i in range (-1*int(panjang),int(panjang)) :
				glVertex3d(0.0,0.0,i)
				glVertex3d(0.0,-1*panjang,i)


		glEnd()



def keyboardSpecial(key, x, y):
	global horizontal
	global vertikal

	if (key == GLUT_KEY_RIGHT) :
		horizontal = horizontal + 5
	elif (key == GLUT_KEY_LEFT) :
		horizontal = horizontal - 5
	elif (key == GLUT_KEY_UP) :
		vertikal = vertikal + 5
	elif (key == GLUT_KEY_DOWN) :
		vertikal = vertikal - 5

	horizontal = horizontal % 360
	vertikal = vertikal % 360
	
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-msk*rasio,+msk*rasio, -msk,+msk, -msk,+msk)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glutPostRedisplay()
	return


def reshape (widthtemp , heighttemp) : 
	global width,height
	widthtemp = width
	heighttemp = height
	rasio = widthtemp / heighttemp
	glViewport(0,0, (widthtemp), (heighttemp))
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(-msk*rasio,+msk*rasio, -msk,+msk, -msk,+msk)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
   


def draw():
	glClearColor( 0, 0, 0, 0);
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
	glMatrixMode( GL_PROJECTION );
	
	glLoadIdentity();
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluPerspective(65, 640/480., .1, 1000)
	glTranslated(0,0,-15)
	
	glRotatef(vertikal,1,0,0);
	glRotatef(horizontal,0,1,0);
    
	kubus(Point, Face, Color)
	grid()
	garis()
	
	glFlush()
	glutSwapBuffers()


def build():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(width, height)
	glutCreateWindow( "3D")
	glutDisplayFunc(draw)
	glutReshapeFunc(reshape)
	glutSpecialFunc(keyboardSpecial)
	glEnable( GL_DEPTH_TEST )
	glutPostRedisplay()
	glutMainLoop()
	if (Command[0]=='exit'):
		glutLeaveMainLoop()
	
def main():
	layar.start()
	
	Keluar = False
	
	while not(Keluar):

			Command = input('Perintah : ').split(' ')
			
			if (Command[0] == 'peek') :
				#Putar ordinat
				if (Command[1] == 'up') :
					rotateyp = True
				elif (Command[1] == 'down') :
					rotateym = True
					#Putar absis
				if (Command[1] == 'left') :
					rotatexp = True
				elif (Command[1] == 'right') :
					rotatexm = True
				
			elif (Command[0] == 'stop') :
				#Putar ordinat berhenti
				rotateyp = False
				rotateym = False
					#Putar absis berhenti
				rotatexp = False
				rotatexm = False
				
			elif (Command[0] == 'translate') :
				dx = float(Command[1])
				dy = float(Command[2])
				dz = float(Command[3])
				
				dxtemp=float(0)
				dytemp=float(0)
				dztemp=float(0)
				
				Ttemp = time.time()
				while((dxtemp+0.001 < dx) or (dytemp+0.001<dy) or (dztemp+0.001<dz)):
					if(dxtemp<=dx):
						dxtemp=dxtemp+0.001
						
					if(dytemp<=dy):
						
						dytemp=dytemp+0.001
					if(dxtemp<=dz):
						dztemp=dztemp+0.001
						#print('testterbaca')
					#print(dxtemp)
					#print(dytemp)
					#print(dztemp)
					
					t3d.Translate(Point, 0.001, 0.001,0.001 )
					time.sleep(0.001)
					glutPostRedisplay()
					#Lakukan hal yg sama pada transformasi lain untuk membuat animasi

			elif (Command[0] == 'dilate') :
				k = float(Command[1])
				t3d.Dilate(Point,k)
			elif (Command[0] == 'rotate') :
				sumbu = Command[1]
				deg = float(Command[2])
				t3d.Rotate(Point,sumbu,deg)
				glutPostRedisplay()
			elif (Command[0] == 'reflect') :
				param = Command[1]
				t3d.Reflect(Point, param)
				glutPostRedisplay()
			elif (Command[0] == 'shear') :
				param = Command[1]
				k = float(Command[2])
				t3d.Shear(Point, param, k)
				glutPostRedisplay()
			elif (Command[0] == 'stretch') :
				param = Command[1]
				k = float(Command[2])
				t3d.Shear(Point, param, k)
				glutPostRedisplay()
			elif (Command[0] == 'custom') :
				a = float(Command[1])
				b = float(Command[2])
				c = float(Command[3])
				d = float(Command[4])
				e = float(Command[5])
				f = float(Command[6])
				g = float(Command[7])
				h = float(Command[8])
				i = float(Command[9])
				t3d.Custom(Point,a,b,c,d,e,f,g,h,i)
				glutPostRedisplay()
			elif (Command[0] == 'multiple') :
				n = int(Command[1])
				t2d.Multiple(Point,n)
				glutPostRedisplay()
			elif (Command[0] == 'reset') :
				for i in range (8) :
					Point[i] = Start[i]
			elif (Command[0] == 'exit') :
				Keluar = True
		
layar = threading.Thread(target = build)
perintah = threading.Thread(target = main)
perintah.start()

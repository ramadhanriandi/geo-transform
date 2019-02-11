import numpy as np
import math

def Translate(Point, dx, dy, dz) :
    for i in range (8) :
        Point[i][0] += dx
        Point[i][1] += dy
        Point[i][2] += dz
    return Point

def Dilate(Point, k) :
    for i in range (8) :
        Point[i] *= k
    return Point

def Rotate(Point, sumbu, deg) :
    deg = np.deg2rad(deg)
    if (sumbu == 'x') :
        # 1 0 0 0
        # 0 cos sin 0
        # 0 -sin cos 0
        # 0 0 0 1
        transformasi=np.matrix([[1, 0, 0, 0],
                               [0, math.cos(deg), math.sin(deg), 0],
                               [0, -1*math.sin(deg), math.cos(deg), 0],
                               [0, 0, 0, 1]])

    elif (sumbu == 'y'):
        # cos 0 sin 0
        # 0 1 0 0
        # -sin 0 cos 0
        # 0 0 0 1
        transformasi=np.matrix([[math.cos(deg), 0, math.sin(deg), 0],
                                [0, 1, 0, 0],
                                [-1*math.sin(deg), 0, math.cos(deg), 0],
                                [0, 0, 0, 1]])
    elif(sumbu =='z'):
        # cos sin 0 0
        # -sin cos 0 0
        # 0 0 1 0
        # 0 0 0 1
        transformasi=np.matrix([[math.cos(deg), math.sin(deg), 0, 0],
                               [-1*math.sin(deg), math.cos(deg), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

    Pointawal=np.matrix([[Point[0][0],Point[1][0],Point[2][0],Point[3][0],Point[4][0],Point[5][0],Point[6][0],Point[7][0]],
                        [Point[0][1],Point[1][1],Point[2][1],Point[3][1],Point[4][1],Point[5][1],Point[6][1],Point[7][1]],
                        [Point[0][2],Point[1][2],Point[2][2],Point[3][2],Point[4][2],Point[5][2],Point[6][2],Point[7][2]],
                        [1,1,1,1,1,1,1,1]])
    
    PointTemp = np.empty([4,4], dtype=float)
    PointTemp=np.dot(transformasi,Pointawal)
    
    for i in range (8):
        for j in range (3):
            Point[i][j]=PointTemp[j,i]

    return Point

def Reflect(Point, param) :
    if (param == 'xz') :
        transformasi=np.matrix([[1, 0, 0, 0],
                               [0, -1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
    elif (param == 'yz') :
        transformasi=np.matrix([[-1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
    elif (param == 'xy') :
        transformasi=np.matrix([[1, 0, 0, 0],
                               [0, 1, 0, 0],
                               [0, 0, -1, 0],
                               [0, 0, 0, 1]])
        
    Pointawal=np.matrix([[Point[0][0],Point[1][0],Point[2][0],Point[3][0],Point[4][0],Point[5][0],Point[6][0],Point[7][0]],
                        [Point[0][1],Point[1][1],Point[2][1],Point[3][1],Point[4][1],Point[5][1],Point[6][1],Point[7][1]],
                        [Point[0][2],Point[1][2],Point[2][2],Point[3][2],Point[4][2],Point[5][2],Point[6][2],Point[7][2]],
                        [1,1,1,1,1,1,1,1]])    
    PointTemp = np.empty([4,4], dtype=float)
    PointTemp=np.dot(transformasi,Pointawal)
    
    for i in range (8):
        for j in range (3):
            Point[i][j]=PointTemp[j,i]

    return Point

def Shear(Point, param, k) :
    hXY, hXZ, hYX, hYZ, hZX, hZY = [0 for i in range(6)]
    if(param == 'xy'):
        hXY = k
    elif(param == 'xz'):
        hXZ = k
    elif(param == 'yx'):
        hYX = k
    elif(param == 'yz'):
        hYZ = k
    elif(param == 'zx'):
        hZX = k
    elif(param == 'zy'):
        hZY = k
        
    transformasi=np.matrix([[1, hYX, hZX, 0],
                           [hXY, 1, hZY, 0],
                           [hXZ, hYZ, 1, 0],
                           [0, 0, 0, 1]])
    
    Pointawal=np.matrix([[Point[0][0],Point[1][0],Point[2][0],Point[3][0],Point[4][0],Point[5][0],Point[6][0],Point[7][0]],
                        [Point[0][1],Point[1][1],Point[2][1],Point[3][1],Point[4][1],Point[5][1],Point[6][1],Point[7][1]],
                        [Point[0][2],Point[1][2],Point[2][2],Point[3][2],Point[4][2],Point[5][2],Point[6][2],Point[7][2]],
                        [1,1,1,1,1,1,1,1]])
    
    PointTemp = np.empty([4,4], dtype=float)
    PointTemp=np.dot(transformasi,Pointawal)
    
    for i in range (8):
        for j in range (3):
            Point[i][j]=PointTemp[j,i]

    return Point

    
def Stretch(Point, param, k) :
    if (param == 'x') :
        for i in range (8) :
            Point[i][0] *= k
    elif (param == 'y') :
        for i in range (8):
            Point[i][1] *= k
    elif (param == 'z') :
        for i in range (8):
            Point[i][2] *= k
    return Point

def Custom (Point, a, b, c, d, e, f, g, h, i) :
    for i in range (8) :
        Ptemp1 = Point[i][0]*a + Point[i][1]*b + Point[i][2]*c
        Ptemp2 = Point[i][0]*d + Point[i][1]*e + Point[i][2]*f
        Ptemp3 = Point[i][0]*g + Point[i][1]*h + Point[i][2]*i
        Point[i][0] = Ptemp1
        Point[i][1] = Ptemp2
        Point[i][2] = Ptemp3
    return Point

def Multiple(Point, n) :
    for i in range(n) :
        Command = input('Tahap %d : ' % (i+1)).split(' ')
        if (Command[0] == 'translate') :
            Point = Translate(Point, float(Command[1]), float(Command[2]), float(Command[3]))
        elif (Command[0] == 'dilate') :
            Point = Dilate(Point, float(Command[1]))
        elif (Command[0] == 'rotate') :
            Point = Rotate(Point, Command[1], float(Command[2]))
        elif (Command[0] == 'reflect') :
            Point = Reflect(Point, Command[1])
        elif (Command[0] == 'shear') :
            Point = Shear(Point, Command[1], float(Command[2]))            
        elif (Command[0] == 'stretch') :
            Point = Stretch(Point, Command[1], float(Command[2]))
        elif (Command[0] == 'custom') :
            Point = Custom(Point, float(Command[1]), float(Command[2]), float(Command[3]), float(Command[4]), float(Command[5]), float(Command[6]), float(Command[7]), float(Command[8]), float(Command[10]))
    return Point

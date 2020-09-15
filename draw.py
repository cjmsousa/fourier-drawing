import tkinter as tk
import math
import cmath
import time
import numpy

from vector import Vector
from animation import Animation

NUMBER_OF_VECTORS_PAIRS = 50

def buildVectors(drawingPoints):

    vectors = []
    for i in range(-NUMBER_OF_VECTORS_PAIRS, NUMBER_OF_VECTORS_PAIRS + 1, 1):

        sum = complex(0, 0)

        for j in range(0, len(drawingPoints)):
            sum += complex(drawingPoints[j][0], drawingPoints[j][1]) * cmath.exp(-i * 2 * math.pi * complex(0, 1) * j / len(drawingPoints))
        
        vector =  Vector(magnitude = abs(sum), phase = numpy.angle(sum), period = i)
        print(vector)
        
        vectors.append(vector)

    print(len(vectors))
    return(vectors)

#Define list of vectors
vectors = [
    Vector(magnitude = 100, phase = 0, period = 1), #1 * e^(it) 
    Vector(magnitude = 75, phase = 1, period = -2), # 1/2 * e^(7it)
    Vector(magnitude = 50, phase = 2.5, period = -3),
    Vector(magnitude = 25, phase = 3, period = 4),  #  1/3 * i *  e ^(−17it)  = 1/3 * pi/2 *  e ^(−17it) 
    Vector(magnitude = 100, phase = 0, period = -1), #1 * e^(it) 
    Vector(magnitude = 75, phase = 1.8, period = -2), # 1/2 * e^(7it)
    Vector(magnitude = 50, phase = 2.5, period = 3),
    Vector(magnitude = 25, phase = 3, period = -4),  #  1/3 * i *  e ^(−17it)  = 1/3 * pi/2 *  e ^(−17it) 
    Vector(magnitude = 10, phase = 3, period = -16),
    Vector(magnitude = 10, phase = 3, period = -17),
    Vector(magnitude = 10, phase = 3, period = 15),
    Vector(magnitude = 10, phase = 3, period = -14),
    Vector(magnitude = 10, phase = 3, period = 13),
    Vector(magnitude = 10, phase = 3, period = -12),
    Vector(magnitude = 10, phase = 3, period = -11),
    Vector(magnitude = 10, phase = 3, period = -1),
    Vector(magnitude = 5, phase = 3, period = 2),
    Vector(magnitude = 5, phase = 3, period = 4),
]

#Create dummy drawing
drawingPoints = []
drawingPoints.append([0, 1])
drawingPoints.append([0, 2])
drawingPoints.append([0, 3])
drawingPoints.append([0, 4])
drawingPoints.append([0, 5])
drawingPoints.append([0, 6])
drawingPoints.append([0, 7])
drawingPoints.append([0, 8])
drawingPoints.append([0, 9])
drawingPoints.append([0, 10])


#Build vector list
#vectors = buildVectors(drawingPoints)

#Create animation
animation = Animation(vectors)

#Run animation
animation.run()

#Wait for events
animation.wait()

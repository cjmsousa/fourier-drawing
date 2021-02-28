import math
import cmath
import numpy as np

from animation import Animation
from user_shape import UserShape
from vector import Vector

NUMBER_OF_VECTORS = 10
CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080

def getVectors(shape):

    #Calculate the timeslices vector. Linearly distribute the number of points between 0 and 1
    timeSlices = np.linspace(0, 1, len(shape))

    #Tranform the list of points of the shape into a time based function
    drawingFunction = []
    for i in range(len(shape)):
        drawingFunction.append((round(timeSlices[i], 4), shape[i]))

    #Calcuate the delta t of the function. I'm being lazy and just using the first function point after t = 0
    deltaT = drawingFunction[1][0]

    #Create a range for the cn vectors, considering the number of vectors defined
    cRange = range(int((NUMBER_OF_VECTORS - 1) / 2 * -1), int((NUMBER_OF_VECTORS - 1) / 2) + 1)
    
    #Calculate the numerical integrate of the function according to the cn = sum(f(t) * e^(-n * 2 * pi * i * t) * deltaT)
    vectors = []
    for n in cRange:
        
        #Calculate cn
        cn = 0
        for drawingPoint in drawingFunction:
            cn = cn + drawingPoint[1] * cmath.exp(-1 * n * 2 * math.pi * 1j * drawingPoint[0]) * deltaT

        #Create vector
        vectors.append(Vector(cn, n))

    return(vectors)

#Get shape to draw
userShape = UserShape(CANVAS_WIDTH, CANVAS_HEIGHT)
userShape.drawShape()
shape = userShape.getShape()

#Get initial vectors
vectors = getVectors(shape)

#Create animation
animation = Animation(vectors)
animation.run()

#Wait for events
animation.wait()

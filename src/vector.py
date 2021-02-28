import tkinter as tk
import math
import cmath
import time

class Vector:
    
    def __init__(self, c, period):

        #Setup vector properties
        self.vector = self.__createVector(c, period)
        self.c = c
        self.period = period
        self.canvasVector = 0
        self.canvasCircle = 0
        self.root = (0, 0)
        self.drawingPoint = (0, 0)

    def move(self, other):

        self.root = (other.root[0] + other.vector.real, other.root[1] + other.vector.imag)
    
    def __createVector(self, c, period, t = 0):
        
        return c * cmath.exp(period * 2 * math.pi * 1j *  t)

    def rotate(self, t):

        self.vector = self.__createVector(self.c, self.period, t)

    def draw(self, canvas):

        #Calculate vector drawing parameters
        xOffset = canvas.winfo_width() / 2
        yOffset = canvas.winfo_height() / 2

        x0 = self.root[0] + xOffset
        y0 = yOffset - self.root[1]
        x1 = self.root[0] + self.vector.real + xOffset
        y1 = yOffset - self.root[1] - self.vector.imag

        #Save drawing point
        self.drawingPoint = (x1, y1)

        #Calculate circle radius
        r = abs(self.vector)
        
        #Check if drawn before
        if (self.canvasVector == 0):
            #Draw vector elements
            self.canvasVector = canvas.create_line(x0, y0, x1, y1, arrow = tk.LAST, width = 2, fill = 'yellow')
            self.canvasCircle = canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, width = 2, fill = '', outline='#777777')
        else:
            #Move vector elements
            canvas.coords(self.canvasVector, x0, y0, x1, y1)
            canvas.coords(self.canvasCircle, x0 - r, y0 - r, x0 + r, y0 + r)


# root = tk.Tk()
# canvas = tk.Canvas(root, width = 1920, height = 1080)
# canvas.configure(background='black')
# canvas.pack()
# canvas.update()

# vector1 = Vector(200, math.pi/4, 1)
# vector1.draw(canvas)
# vector1.rotate(0.5)
# vector1.draw(canvas)


# vector2 = Vector(100, math.pi/2, -1)
# vector2.move(vector1)
# vector2.draw(canvas)
# vector3 = Vector(50, math.pi, 1)

# vector1.rotate(0.5)

# vector2.move(vector1)
# vector3.move(vector2)


# vector3.draw(canvas)

# root.mainloop()
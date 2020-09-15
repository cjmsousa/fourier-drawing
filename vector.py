import tkinter as tk
import math

class Vector:
    
    #Define vector properties
    value = complex(0, 0)
    period = 1
    __canvasLine = 0
    __canvasCircle = 0

    def __init__(self, value, period):

        #Setup vector properties
        self.value = value
        self.period = period
    
    def move(self, t):

        #Define root coordinates
        self.x0 = x
        self.y0 = y

        #Calculate new angle
        angle = self.phase + 2 * math.pi * math.modf(t)[0] * self.period

        #Calculate new coordinates and update vector
        self.x1 = self.x0 + math.cos(angle) * self.magnitude
        self.y1 = self.y0 + math.sin(angle) * self.magnitude

    def draw(self, canvas):

        #Check if drawn before
        if (self.__canvasLine == 0):

            #Draw vector elements
            self.__canvasLine = canvas.create_line(self.x0, self.y0, self.x1, self.y1, arrow = tk.LAST, width = 2, fill = 'yellow')
            self.__canvasCircle = canvas.create_oval(self.x0 - self.magnitude, self.y0 - self.magnitude, self.x0 + self.magnitude, self.y0 + self.magnitude, width = 2, fill = '', outline='#777777')

        else:

            #Move vector elements
            canvas.coords(self.__canvasLine, self.x0, self.y0, self.x1, self.y1)
            canvas.coords(self.__canvasCircle, self.x0 - self.magnitude, self.y0 - self.magnitude, self.x0 + self.magnitude, self.y0 + self.magnitude)

    def __str__(self):

        #Print vector
        return("value = [{}]".format(self.value))
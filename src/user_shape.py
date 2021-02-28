import tkinter as tk
import time as time

class UserShape:

    def __init__(self, width, height):

        #Create canvas objects
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = width, height = height)
        self.canvas.configure(background='black')
        self.canvas.pack()
        self.canvas.update()

        #Define class properties
        self.width = width
        self.height = height
        self.shapePoint = None
        self.capturing = False
        self.shape = []

    def switchCaptureMode(self, event):

        #Switch capturing mode
        self.capturing = not self.capturing

        #End capturing after done
        if (not self.capturing):
            self.root.destroy()

    def draw(self, event):

        #Only draw if capturing
        if (self.capturing):

            #Save point as part of the shape
            self.shape.append((event.x, event.y))
            
            #Draw shape in screen
            if self.shapePoint: 
                self.canvas.create_line(event.x, event.y, self.shapePoint[0], self.shapePoint[1], width = 2, fill = 'red') 
            
            #Save current point
            self.shapePoint = (event.x, event.y)
    
    def drawShape(self):

        #Bind mouse events
        self.root.bind('<ButtonPress-1>', self.switchCaptureMode)
        self.root.bind('<Motion>', self.draw)

        #Run drawing
        self.root.mainloop()

    def getShape(self):

        #Calculate shape positioning parameters
        xOffset = self.width / 2
        yOffset = self.height / 2

        self.shape = [((point[0] - xOffset) / 1, (yOffset - point[1]) / 1) for point in self.shape]

        #Change shape axis to center around root and transform in imaginary coordinates
        for i in range(len(self.shape)):
            self.shape[i] = self.shape[i][0] + self.shape[i][1] * 1j
        
        return(self.shape)
import tkinter as tk
import time as time

class Animation:

    #Define constants
    DRAW_INTERVAL_MILISECONDS = 5
    SLOW_MOTION_FACTOR = 20

    def __init__(self, vectors):

        #Create canvas objects
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = 1920, height = 1080)
        self.canvas.configure(background='black')
        self.canvas.pack()
        self.canvas.update()

        self.vectors = vectors
        self.startTime = 0
        self.lastPointOnPath = None

    def __sumVectors(self):
        
        # Needs more than 1 vector to run
        if (len(self.vectors) > 1): 

            #Go for all vectors
            for i in range(len(self.vectors) - 1):
            
                # Move next vector to the tip of the current
                self.vectors[i + 1].move(self.vectors[i])

    def __tracePath(self):

        #Draw a line between last point and current to complete trace path
        if (self.lastPointOnPath != None):

            self.canvas.create_line(self.lastPointOnPath[0], self.lastPointOnPath[1], self.vectors[-1].drawingPoint[0], self.vectors[-1].drawingPoint[1],  width = 2, fill = 'red')

        #Edit last point
        self.lastPointOnPath = (self.vectors[-1].drawingPoint[0], self.vectors[-1].drawingPoint[1])
    
    def run(self):

        #Set start time if needed and calculate elapsed time
        self.startTime = self.startTime if self.startTime != 0 else time.time()
        t = (time.time() - self.startTime) / self.SLOW_MOTION_FACTOR

        #Rotate vectors
        [vector.rotate(t) for vector in self.vectors]

        #Sum all vectors
        self.__sumVectors()

        #Draw vectors
        [vector.draw(self.canvas) for vector in self.vectors]

        #Trace path for last vector
        self.__tracePath()

        #Start draw loop
        self.root.after(self.DRAW_INTERVAL_MILISECONDS, self.run)

    def wait(self):
        
        #Event loop
        self.root.mainloop()
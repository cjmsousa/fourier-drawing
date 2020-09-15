import tkinter as tk
import time as time

class Animation:

    #Define constants
    SLOW_MOTION_FACTOR = 100
    DRAW_INTERVAL_MILISECONDS = 5

    #Define animation properties
    root = 0
    canvas = 0
    startTime = 0
    vectors = []
    lastPathPoint = []

    def __init__(self, vectors):

        #Setup animation properties
        self.vectors = vectors

        #Create canvas objects
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = 1920, height = 1080)
        self.canvas.configure(background='black')
        self.canvas.pack()
        self.canvas.update()

    def __sum(self, t):
        
        #Move vectors
        [vector.move(t) for vector in self.vectors]

        #Sum all vectors
        sum(self.vectors)

    def tracePath(self):

        #Draw a line between last point and current to complete trace path
        if (len(self.lastPathPoint) > 0):
            self.canvas.create_line(self.lastPathPoint[0], self.lastPathPoint[1], self.vectors[-1].x1, self.vectors[-1].y1,  width = 2, fill = 'red')

        #Edit last point
        self.lastPathPoint = [self.vectors[-1].x1, self.vectors[-1].y1]
    
    def run(self):

        #Set start time if needed
        self.startTime = self.startTime if self.startTime == 0 else time.time()

        #Calculate elapsed time
        t = (time.time() - self.startTime) / self.SLOW_MOTION_FACTOR

        #Chain vectors
        self.__chain(t)

        #Draw vectors
        [vector.draw(self.canvas) for vector in self.vectors]

        #Trace path for last vector
        self.tracePath()

        #Start draw loop
        self.root.after(self.DRAW_INTERVAL_MILISECONDS, self.run)

    def wait(self):

        #Event loop
        self.root.mainloop()
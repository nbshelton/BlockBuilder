from tkinter import *
from bb_shapes import *

class tCell(Canvas):
    baseColor = '#E4E4E4'
    def __init__(self, master, size=20, bgcolor=baseColor):
        self.filled = False
        Canvas.__init__(self, master, width=size, height=size, bd=2, bg=bgcolor, highlightthickness=0, relief=RAISED)

    def setColor(self, newcolor):
        self.configure(bg=newcolor)

    def fill(self, newColor):
        self.filled = True
        self.configure(bg=newColor)

    def unfill(self):
        self.filled = False
        self.configure(bg=self.baseColor)
        

class tField(Frame):
    def __init__(self, master, cellsize=20, cols=10, rows=22):
        self.CELLSIZE = cellsize
        self.ROWS = rows
        self.COLS = cols
        self.WIDTH = cellsize*cols
        self.HEIGHT = cellsize*rows
        Frame.__init__(self, master)
        self.grid()
        self.populateEmpty()
        self.forgetTopRows(2)

    def populateEmpty(self):
        self.cells = {}
        for x in range(self.COLS):
            for y in range(self.ROWS):
                cell = tCell(self, self.CELLSIZE)
                self.cells[(x,y)] = cell
                cell.grid(column=x, row=y)

    def forgetTopRows(self, rows):
        for y in range(rows):
            for x in range(self.COLS):
                self.cells[(x,y)].grid_remove()

    def getEnvironment(self, tlx, tly):
        return {(dx,dy): (1 if (self.cells.get((tlx+dx,tly+dy), None) is None
                                or self.cells[(tlx+dx,tly+dy)].filled)
                          else 0)
                for dx in range(4)
                for dy in range(4)}

    def checkDownCollision(self):
        self.undrawShape()
        return self.checkCollision(dy=1)
    def checkRightCollision(self):
        self.undrawShape()
        return self.checkCollision(dx=1)
    def checkLeftCollision(self):
        self.undrawShape()
        return self.checkCollision(dx=-1)
    def checkCollision(self, dx=0, dy=0):
        if self.shape is None:
            return False
        shapeCells = self.shape.getCells()
        environment = self.getEnvironment(self.shapex+dx, self.shapey+dy)
        collision = any(shapeCells[(x,y)]*environment[(x,y)] == 1
                        for x in range(4)
                        for y in range(4))
        return collision

    def undrawShape(self):
        self.drawShape(False)
    def drawShape(self, fill=True):
        x = self.shapex
        y = self.shapey
        shapeCells = self.shape.getCells()
        if fill:
            color = self.shape.color
            for (dx,dy) in shapeCells:
                if (shapeCells[(dx,dy)] == 1):
                    try:
                        self.cells[(x+dx,y+dy)].fill(color)
                    except KeyError:
                        pass
        else:
            for (dx,dy) in shapeCells:
                if (shapeCells[(dx,dy)] == 1):
                    try:
                        self.cells[(x+dx,y+dy)].unfill()
                    except KeyError:
                            pass

    def dropShape(self):
        if self.checkDownCollision():
            self.merge()
        else:
            self.shapey += 1
            self.drawShape()

    def merge(self):
        self.drawShape()
        self.checkLines()
        self.checkEnd()
        self.shape = randomShape()
        self.shapex = 3
        self.shapey = 0

    def checkLines(self):
        for y in range(self.ROWS):
            if not any(not self.cells[(x,y)].filled
                       for x in range(self.COLS)):
                self.eliminateRow(y)

    def eliminateRow(self, y):
        if y==0:
            for x in range(self.COLS):
                self.cells[(x,y)].unfill()
            return
        
        for x in range(self.COLS):
            if self.cells[(x,y-1)].filled:
                self.cells[(x,y)].fill(self.cells[(x,y-1)]["background"])
            else:
                self.cells[(x,y)].unfill()
        self.eliminateRow(y-1)

    def checkEnd(self):
        pass

def init(app):
    app.shape = randomShape()
    app.shapex=3
    app.shapey=0
    app.after(1000, cont, app)

def cont(field):
    field.dropShape()
    if field.shape is not None:
        field.after(1000, cont, field)

def uppress(event):
    app.undrawShape()
    app.shape.reorient()
    for x in range(4):
        if not app.checkCollision(dx=x):
            app.shapex += x
            app.drawShape()
            return
        if not app.checkCollision(dx=0-x):
            app.shapex -= x
            app.drawShape()
            return
    app.shape.unorient()
    app.drawShape()

def downpress(event):
    if not app.checkDownCollision():
        app.shapey += 1
        app.drawShape()
    else:
        app.merge()

def rightpress(event):
    if not app.checkRightCollision():
        app.shapex += 1
    app.drawShape()

def leftpress(event):
    if not app.checkLeftCollision():
        app.shapex -= 1
    app.drawShape()

app = tField(None)
app.master.title('BlockBuilder')
app.bind_all('<Right>', rightpress)
app.bind_all('<Left>', leftpress)
app.bind_all('<Down>', downpress)
app.bind_all('<Up>', uppress)
app.focus_set()
init(app)
app.mainloop()

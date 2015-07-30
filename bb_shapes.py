from enum import Enum
from random import randrange

class Orientation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

def randomShape():
    si = randrange(0, 7)
    if si == 0:
        return SquareShape()
    elif si == 1:
        return LineShape()
    elif si == 2:
        return SnakeShape()
    elif si == 3:
        return ReverseSnakeShape()
    elif si == 4:
        return LShape()
    elif si == 5:
        return ReverseLShape()
    else:
        return TShape()

class Shape(object):
    def __init__(self, cells, color):
        self.orient = Orientation.UP
        self.cells = cells
        self.color = color

    def reorient(self):
        self.orient = Orientation((self.orient.value-1)%4)

    def unorient(self):
        self.orient = Orientation((self.orient.value+1)%4)

    def getCells(self):
        return {(x,y): self.cells[self.orient.value][y][x]
                for x in range(4)
                for y in range(4)}

class SquareShape(Shape):
    def __init__(self):
        cells = {x: ((0,1,1,0),
                     (0,1,1,0),
                     (0,0,0,0),
                     (0,0,0,0))
                 for x in range(4)}
        Shape.__init__(self, cells, '#ffff00')

class LineShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (1, 1, 1, 1),
                                       (0, 0, 0, 0),
                                       (0, 0, 0, 0))
        cells[Orientation.RIGHT.value] = ((0, 0, 1, 0),
                                          (0, 0, 1, 0),
                                          (0, 0, 1, 0),
                                          (0, 0, 1, 0))
        cells[Orientation.DOWN.value] = cells[Orientation.UP.value]
        cells[Orientation.LEFT.value] = cells[Orientation.RIGHT.value]
        Shape.__init__(self, cells, '#0099ff')

class SnakeShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (0, 0, 0, 0),
                                       (0, 0, 1, 1),
                                       (0, 1, 1, 0))
        cells[Orientation.RIGHT.value] = ((0, 0, 0, 0),
                                          (0, 0, 1, 0),
                                          (0, 0, 1, 1),
                                          (0, 0, 0, 1))
        cells[Orientation.DOWN.value] = cells[Orientation.UP.value]
        cells[Orientation.LEFT.value] = cells[Orientation.RIGHT.value]
        Shape.__init__(self, cells, '#00ff00')

class ReverseSnakeShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (0, 0, 0, 0),
                                       (0, 1, 1, 0),
                                       (0, 0, 1, 1))
        cells[Orientation.RIGHT.value] = ((0, 0, 0, 0),
                                          (0, 0, 0, 1),
                                          (0, 0, 1, 1),
                                          (0, 0, 1, 0))
        cells[Orientation.DOWN.value] = cells[Orientation.UP.value]
        cells[Orientation.LEFT.value] = cells[Orientation.RIGHT.value]
        Shape.__init__(self, cells, '#ff0000')

class LShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (0, 0, 0, 0),
                                       (0, 0, 0, 1),
                                       (0, 1, 1, 1))
        cells[Orientation.RIGHT.value] = ((0, 0, 0, 0),
                                          (0, 0, 1, 1),
                                          (0, 0, 0, 1),
                                          (0, 0, 0, 1))
        cells[Orientation.DOWN.value] = ((0, 0, 0, 0),
                                         (0, 0, 0, 0),
                                         (0, 1, 1, 1),
                                         (0, 1, 0, 0))
        cells[Orientation.LEFT.value] = ((0, 0, 0, 0),
                                         (0, 0, 1, 0),
                                         (0, 0, 1, 0),
                                         (0, 0, 1, 1))
        Shape.__init__(self, cells, '#ff9900')

class ReverseLShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (0, 0, 0, 0),
                                       (0, 1, 0, 0),
                                       (0, 1, 1, 1))
        cells[Orientation.RIGHT.value] = ((0, 0, 0, 0),
                                          (0, 0, 0, 1),
                                          (0, 0, 0, 1),
                                          (0, 0, 1, 1))
        cells[Orientation.DOWN.value] = ((0, 0, 0, 0),
                                         (0, 0, 0, 0),
                                         (0, 1, 1, 1),
                                         (0, 0, 0, 1))
        cells[Orientation.LEFT.value] = ((0, 0, 0, 0),
                                         (0, 0, 1, 1),
                                         (0, 0, 1, 0),
                                         (0, 0, 1, 0))
        Shape.__init__(self, cells, '#0000ff')

class TShape(Shape):
    def __init__(self):
        cells = {}
        cells[Orientation.UP.value] = ((0, 0, 0, 0),
                                       (0, 0, 0, 0),
                                       (0, 0, 1, 0),
                                       (0, 1, 1, 1))
        cells[Orientation.RIGHT.value] = ((0, 0, 0, 0),
                                          (0, 0, 0, 1),
                                          (0, 0, 1, 1),
                                          (0, 0, 0, 1))
        cells[Orientation.DOWN.value] = ((0, 0, 0, 0),
                                         (0, 1, 1, 1),
                                         (0, 0, 1, 0),
                                         (0, 0, 0, 0))
        cells[Orientation.LEFT.value] = ((0, 0, 0, 0),
                                         (0, 1, 0, 0),
                                         (0, 1, 1, 0),
                                         (0, 1, 0, 0))
        Shape.__init__(self, cells, '#ff00ff')

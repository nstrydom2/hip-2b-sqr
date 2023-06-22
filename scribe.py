import os
import time


class Canvas:
    _x: int
    _y: int
    _canvas: list

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._canvas = [[' ' for _ in range(self._y)] for _ in range(self._x)]

    def hits_wall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def print(self):
        self.refresh()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

    def set_item(self,  x, y, ch='.'):
        self._canvas[x][y] = ch

    def refresh(self):
        os.system('cls')


class Scribe:
    _canvas: Canvas

    def __init__(self, canvas_x=2, canvas_y=2):
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]
        self._canvas = Canvas(x=canvas_x, y=canvas_y)

    def draw_square(self, w, l):
        for _ in range(w):
            self.right()

        for _ in range(l):
            self.down()

        for _ in range(w):
            self.left()

        for _ in range(l):
            self.up()

    def draw_shape(self, shape):
        for y_idx, y in enumerate(shape):
            for x_idx, x in enumerate(y):
                if x not in ['', ' ']:
                    self.draw([x_idx, y_idx])

    def draw_stairs(self, steps=4):
        for _ in range(steps):
            self.right()
            self.right()
            self.right()
            self.down()
            self.down()

        while self.pos[0] > 0:
            self.left()

        while self.pos[1] > 1:
            self.up()

    def right(self, steps: int = 1):
        pos = [self.pos[0]+steps, self.pos[1]]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def left(self, steps: int = 1):
        pos = [self.pos[0]-steps, self.pos[1]]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def up(self, steps: int = 1):
        pos = [self.pos[0], self.pos[1]-steps]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def down(self, steps: int = 1):
        pos = [self.pos[0], self.pos[1]+steps]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def draw(self, pos):
        self._canvas.set_item(self.pos[0], self.pos[1], self.trail)
        self.pos = pos
        self._canvas.set_item(self.pos[0], self.pos[1], self.mark)
        self._canvas.print()
        time.sleep(self.framerate)

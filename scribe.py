import os
import time


class Canvas:
    _x: int
    _y: int
    _canvas: list

    def __init__(self, window_dims):
        self._x, self._y = window_dims
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
    _direction: int

    def __init__(self, canvas_dims=(4, 4)):
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.21
        self.pos = [0, 0]
        self._canvas = Canvas(window_dims=canvas_dims)
        self._direction = 90

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
        self._direction = 90

        pos = [self.pos[0]+steps, self.pos[1]]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def left(self, steps: int = 1):
        self._direction = 270

        pos = [self.pos[0]-steps, self.pos[1]]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def up(self, steps: int = 1):
        self._direction = 0

        pos = [self.pos[0], self.pos[1]-steps]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def down(self, steps: int = 1):
        self._direction = 180

        pos = [self.pos[0], self.pos[1]+steps]
        if not self._canvas.hits_wall(self.pos):
            self.draw(pos)

    def forward(self):
        if self._direction == 90:
            self.right()
        elif self._direction == 0:
            self.up()
        elif self._direction == 180:
            self.down()
        elif self._direction == 270:
            self.left()

    def draw(self, pos):
        self._canvas.set_item(self.pos[0], self.pos[1], self.trail)
        self.pos = pos
        self._canvas.set_item(self.pos[0], self.pos[1], self.mark)
        self._canvas.print()
        time.sleep(self.framerate)

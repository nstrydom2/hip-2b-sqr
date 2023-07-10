import os
import time

from typing import List


class Canvas:
    _x: int
    _y: int
    _canvas: list

    def __init__(self, window_dims):
        self._x, self._y = window_dims
        self._canvas = [[' ' for _ in range(self._y)] for _ in range(self._x)]

    def hits_wall(self, point):
        return round(point[0]) < 0 or round(point[0]) >= self._x or round(point[1]) < 0 or round(point[1]) >= self._y

    def print(self):
        self.refresh()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

    def set_item(self,  x, y, ch='.'):
        self._canvas[round(x)][round(y)] = ch

    def refresh(self):
        os.system('cls')


class Scribe:
    _canvas: Canvas

    def __init__(self, canvas_dims=(4, 4)):
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.21
        self._canvas = Canvas(window_dims=canvas_dims)
        self._pos = [0, 0]

        self._direction = [0, 1]

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

        while self._pos[0] > 0:
            self.left()

        while self._pos[1] > 1:
            self.up()

    def direction_deg(self, degrees):
        radians = (degrees / 180) * math.pi
        self._direction = [math.sin(radians), -math.cos(radians)]

    def right(self, steps: int = 1):
        self._direction = [1, 0]
        self.forward()

    def left(self, steps: int = 1):
        self._direction = [-1, 0]
        self.forward()

    def up(self, steps: int = 1):
        self._direction = [0, -1]
        self.forward()

    def down(self, steps: int = 1):
        self._direction = [0, 1]
        self.forward()

    def forward(self):
        pos = [self._pos[0] + self._direction[0], self._pos[1] + self._direction[1]]
        if not self._canvas.hits_wall(pos):
            self.draw(pos)

    def draw(self, pos):
        self._canvas.set_item(self._pos[0], self._pos[1], self.trail)
        self._pos = pos
        self._canvas.set_item(self._pos[0], self._pos[1], self.mark)
        self._canvas.print()
        time.sleep(self.framerate)

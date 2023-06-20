import os
import time


class Canvas:
    _x: int = 3
    _y: int = 3
    _canvas: list = [['' for _ in range(4)] for _ in range(4)]

    def draw(self):
        for row in self._canvas:
            for col in row:
                print(col, end="   ")
            print(end="\n\n")

    def set_item(self,  x, y, ch='.'):
        self._canvas[x][y] = ch

    def refresh(self):
        os.system('cls')


class Scribe:
    _cursor_x: int = 0
    _cursor_y: int = 0
    _canvas: Canvas = Canvas()

    def draw_square(self, w, l):
        for x in range(w):
            for y in range(l):
                self._canvas.refresh()
                self._canvas.set_item(x, y)
                self._canvas.draw()
                time.sleep(1)

    def draw_shape(self, shape):
        for x_idx, x in enumerate(shape):
            for y_idx, y in enumerate(x):
                self._canvas.refresh()
                self._canvas.set_item(x_idx, y_idx, y)
                self._canvas.draw()

                if y != ' ':
                    time.sleep(1)

    def right(self, steps: int = 1):
        self._cursor_x += steps

    def left(self, steps: int = 1):
        self._cursor_x -= steps

    def up(self, steps: int = 1):
        self._cursor_y -= steps

    def down(self, steps: int = 1):
        self._cursor_y += steps

    def draw(self):
        for i in range(self.cursor_x):
            print(f".", end=" ")

        print(end="\n")
        for i in range(self.cursor_y):
            whitespace = ' ' * (self.cursor_x + 1)
            print(f"{whitespace}.", end="\n")

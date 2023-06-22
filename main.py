# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from scribe import Scribe


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    shape = [
        ['.', '.', '.'],
        ['.', '', '.'],
        ['.', '.', '.'],
    ]

    scribe = Scribe(20, 20)
    #scribe.draw_stairs(6)
    #scribe.draw_square(5, 5)
    #scribe.draw_shape(shape)
    scribe.draw_shape(shape)


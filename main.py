# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List, Dict
from scribe import Scribe


def run_multi_scribe(scribes: Dict):
    for scribe, instructions in scribes.values():
        for instruction, steps in instructions:
            if instruction == 'up':
                scribe.up(steps)
            elif instruction == 'down':
                scribe.down(steps)
            elif instruction == 'left':
                scribe.left(steps)
            elif instruction == 'right':
                scribe.right(steps)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # shape = [
    #     ['.', '.', '.'],
    #     ['.', '', '.'],
    #     ['.', '.', '.'],
    # ]
    #
    # scribe = Scribe(canvas_dims=(30, 30))
    # #scribe.draw_stairs(6)
    # scribe.draw_square(20, 20)

    robots = {'gary': [
        Scribe(canvas_dims=(30, 30), start_pos=[0, 0]),
        [
            (up, 5),
            (down, 5),
            (left, 5),
            (right, 5)
        ],
    ],
    'george': [
        Scribe(canvas_dims=(30, 30), start_pos=[10, 10]),
        [
            (up, 5),
            (down, 5),
            (left, 5),
            (right, 5)
        ],
    ],
    }
    run_multi_scribe(scribes=robots)


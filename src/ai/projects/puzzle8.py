import numpy as np
from algorithms.search import Search

GOAL = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0], dtype=np.int8)

MOVE = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}


class Puzzle8:

    def __init__(self, start):
        self.start = np.array(start, dtype=np.int8)

    def is_goal(self, state):
        return np.array_equal(state, GOAL)

    def start_state(self):
        return self.start

    def neighbors(self, state):
        zero_index = int(np.argwhere(state == 0)[0][0])
        row, column = divmod(zero_index, 3)
        result = []
        for move, (dr, dc) in MOVE.items():
            new_row, new_column = row + dr, column + dc
            if 0 <= new_row < 3 and 0 <= new_column < 3:
                new_zero = new_row * 3 + new_column
                new = state.copy()
                new[zero_index], new[new_zero] = new[new_zero], new[zero_index]
                result.append((move, new))
        return result

    def key(self, state):
        return tuple(state)


#---------------TESTS----------------
test = (1, 2, 3,
         4, 0, 5,
         7, 8, 6)

problem = Puzzle8(test)
path, explored = Search.bfs(problem)
if path is None:
    print(f"حل نشد | explored={explored}")
else:
    print(f"طول={len(path)} | {path} | explored={explored}")
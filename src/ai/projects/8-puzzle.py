import numpy as np
from algorithms.search import Search
from datastructures.stack import Stack
from datastructures.queue import Queues
from algorithms.search import Search


GOAL = np.array([1, 2, 3, 4, 5, 6, 7, 8, 0], dtype=np.int8)

MOVES = {
    "U": (-1, 0),
    "D": ( 1, 0),
    "L": ( 0, -1),
    "R": ( 0,  1),
}


class Puzzle8:

    def __init__(self, start):
        self.start = np.array(start, dtype=np.int8)

    def start_state(self):
        return self.start

    def is_goal(self, state):
        return np.array_equal(state, GOAL)

    def neighbors(self, state):
        zero = int(np.argwhere(state == 0)[0][0])
        r, c = divmod(zero, 3)
        result = []
        for move, (dr, dc) in MOVES.items():
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                new = state.copy()
                new[zero], new[nz] = new[nz], new[zero]
                result.append((move, new))
        return result

    def key(self, state):
        return state.tobytes()

start = (1, 2, 3,
         4, 0, 5,
         7, 8, 6)

problem = Puzzle8(start)
path, explored = Search.bfs(problem)
if path is None:
    print(f"حل نشد | explored={explored}")
else:
    print(f"طول={len(path)} | {path} | explored={explored}")
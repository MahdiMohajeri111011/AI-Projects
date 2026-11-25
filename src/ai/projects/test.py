from collections import deque
import random
from ai.projects.puzzle8 import GOAL, Puzzle8


class PuzzleGenerator:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self._by_depth = self._collect_states(12)

    @staticmethod
    def _collect_states(max_steps):
        helper = Puzzle8(GOAL)
        by_depth = {d: [] for d in range(max_steps + 1)}
        visited = {GOAL: 0}
        queue = deque([(GOAL, 0)])
        by_depth[0].append(GOAL)

        while queue:
            state, dist = queue.popleft()
            if dist >= max_steps:
                continue

            for _, prev_state in helper.neighbors(state):
                if prev_state not in visited:
                    visited[prev_state] = dist + 1
                    queue.append((prev_state, dist + 1))
                    by_depth[dist + 1].append(prev_state)

        return by_depth

    def generate_4_steps(self):
        return self.rng.choice(self._by_depth[4])

    def generate_8_steps(self):
        return self.rng.choice(self._by_depth[8])

    def generate_12_steps(self):
        return self.rng.choice(self._by_depth[12])
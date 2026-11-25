from src.datastructures.queue import Queues
from src.datastructures.stack import Stack

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVE = {
    "U" : (-1 , 0),
    "D" : (1 , 0),
    "L" : (0 , -1),
    "R" : (0 , 1)
}


class Puzzle8 :

    def __init__(self , start):
        self.start = start

    def is_goal(self, state):
        return state == GOAL

    def start_state(self):
        return self.start

    def neighbors(self , state):
        zero = state.index(0)
        row , column = divmod(zero , 3)
        result = []
        for move , (dr , dc) in MOVE.items() :

            new_row, new_column = row + dr , column + dc
            if 0 <= new_row < 3 and 0 <= new_column < 3 :
                new_zero = new_row * 3 + new_column
                new = list(state)
                new[zero] , new[new_zero] = new[new_zero] , new[zero]

            result.append((move , tuple(new)))

        return result

    def key(self, state):
        return tuple(state)


class Search :

    @classmethod
    def bfs(cls , problem : Puzzle8):
        start = problem.start_state()

        if problem.is_goal(start) :
            return [] , 0

        q =  Queues.Queue()
        q.enqueue((start , ""))
        visited = {problem.key(start)}
        explored = 0

        while not q.is_empty() :
            state, path = q.dequeue()
            explored += 1

            for move , nxt in problem.neighbors(state) :
                key = problem.key(nxt)
                if key in visited :
                    continue

                if problem.is_goal(nxt):
                    return path + move, explored

                visited.add(key)
                q.enqueue((nxt, path + move))

        return None , explored

    @classmethod
    def dfs(cls, problem : Puzzle8):
        start = problem.start_state()

        if problem.is_goal(start) :
            return [], 0

        stack = Stack()
        stack.push((start , ""))
        visited = {problem.key(start)}
        explored = 0

        while not stack.is_empty() :
            path , state = stack.pop()
            explored += 1

            for move , nxt in problem.neighbors() :

                 key = problem.key(nxt)
                 if key in visited :
                     continue

                 if problem.is_goal(nxt) :
                     return move + path , explored

                 visited.add(key)
                 stack.push((nxt , path + move))

            return None , explored

    @classmethod
    def ids(cls, problem : Puzzle8):
        start = problem.start_state()

        if problem.is_goal(start) :
            pass
            

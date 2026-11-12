from datastructures.queue import Queues
from datastructures.stack import Stack
from utilities.decorators import timer

class Search:

    @timer
    @classmethod
    def bfs(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        q = Queues.Queue()
        q.enqueue((start, ""))
        visited = {problem.key(start)}
        explored = 0

        while not q.is_empty():
            state, path = q.dequeue()
            explored += 1

            for move, nxt in problem.neighbors(state):
                key = problem.key(nxt)
                if key in visited:
                    continue
                if problem.is_goal(nxt):
                    return path + move, explored
                visited.add(key)
                q.enqueue((nxt, path + move))

        return None, explored

    @timer
    @classmethod
    def dfs(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        stack = Stack()
        stack.push((start, ""))
        visited = {problem.key(start)}
        explored = 0

        while not stack.is_empty():
            state, path = stack.pop()
            explored += 1

            if problem.is_goal(state):
                return path, explored

            for move, nxt in problem.neighbors(state):
                key = problem.key(nxt)
                if key in visited:
                    continue
                visited.add(key)
                stack.push((nxt, path + move))

        return None, explored


    @timer
    @classmethod
    def ids(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        explored = 0
        limit = 0

        while True:
            stack = Stack()
            stack.push((start, "", 0))

            while not stack.is_empty():
                state, path, depth = stack.pop()
                explored += 1

                if problem.is_goal(state):
                    return path, explored

                if depth >= limit:
                    continue

                for move, nxt in problem.neighbors(state):
                    stack.push((nxt, path + move, depth + 1))

            limit += 1
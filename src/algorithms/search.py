from datastructures.queue import Queues
from datastructures.stack import Stack
from utilities.decorators import timer

class Search:

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

    @classmethod
    def ucs(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        hq = Queues.HeapQueue()
        hq.enqueue((0, start, ""))
        visited = {problem.key(start): 0}
        explored = 0

        while not hq.is_empty():

            cost, state, path = hq.dequeue()
            explored += 1

            if problem.is_goal(state):
                return path, explored

            for move, nxt in problem.neighbors(state):
                new_cost = cost + 1
                key = problem.key(nxt)

                if key in visited and visited[key] <= new_cost:
                    continue

                visited[key] = new_cost
                hq.enqueue((new_cost, nxt, path + move))

        return None, explored

    @classmethod
    def astar(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        hq = Queues.HeapQueue()
        h_start = problem.manhattan(start)
        hq.enqueue((h_start, 0, start, ""))

        best_g = {problem.key(start): 0}
        explored = 0

        while not hq.is_empty():
            _, g_cost, state, path = hq.dequeue()
            explored += 1

            if problem.is_goal(state):
                return path, explored

            for move, nxt in problem.neighbors(state):
                new_g = g_cost + 1
                key = problem.key(nxt)

                if key in best_g and best_g[key] <= new_g:
                    continue

                best_g[key] = new_g
                h_cost = problem.manhattan(nxt)
                f_cost = new_g + h_cost
                hq.enqueue((f_cost, new_g, nxt, path + move))

        return None, explored

    @classmethod
    def astar_tiles(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        hq = Queues.HeapQueue()
        h_start = problem.misplaced_tiles(start)
        hq.enqueue((h_start, 0, start, ""))

        best_g = {problem.key(start): 0}
        explored = 0

        while not hq.is_empty():
            _, g_cost, state, path = hq.dequeue()
            explored += 1

            if problem.is_goal(state):
                return path, explored

            for move, nxt in problem.neighbors(state):
                new_g = g_cost + 1
                key = problem.key(nxt)

                if key in best_g and best_g[key] <= new_g:
                    continue

                best_g[key] = new_g
                h_cost = problem.misplaced_tiles(nxt)
                f_cost = new_g + h_cost
                hq.enqueue((f_cost, new_g, nxt, path + move))

        return None, explored
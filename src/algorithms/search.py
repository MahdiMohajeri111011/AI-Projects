from datastructures.queue import Queues


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
    def dfs(cls):
        pass

    @classmethod
    def ids(cls):
        pass


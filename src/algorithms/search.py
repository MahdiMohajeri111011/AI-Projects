from datastructures.queue import Queues


class Search:

    @classmethod
    def bfs(cls, problem):
        start = problem.start_state()

        if problem.is_goal(start):
            return [], 0

        hq = Queues.HeapQueue(max_size=500_000)
        hq.enqueue((0, 0, start, ""))
        counter = 1
        visited = {problem.key(start)}
        explored = 0

        while not hq.is_empty():
            depth, _, state, path = hq.dequeue()
            explored += 1

            for move, nxt in problem.neighbors(state):
                key = problem.key(nxt)
                if key in visited:
                    continue
                if problem.is_goal(nxt):
                    return path + move, explored
                visited.add(key)
                hq.enqueue((depth + 1, counter, nxt, path + move))
                counter += 1

        return None, explored

    @classmethod
    def dfs(cls, problem):
        pass

    @classmethod
    def ids(cls, problem):
        pass
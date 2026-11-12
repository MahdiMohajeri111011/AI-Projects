from datastructures.queue import Queues
from src.ai.projects.puzzle8 import Puzzle8
class Search :

    @classmethod
    def bfs(cls, problom : Puzzle8):
        start = problom.start_state()

        if problom.is_goal(start) :
            return [] , 0

        q = Queues.Queue
        visited = {problom.key(start)}
        explored = 0

        while not q.is_empty() :
            state , path = q.dequeue()
            explored += 1

            for move , nxt in problom.neighbors(state):
                key = problom.key(nxt)
                if nxt in visited :
                    continue
                if problom.is_goal(key) :
                    return path + move, explored
                visited.add(key)
                q.enqueue((nxt , path + move))

            return None, explored
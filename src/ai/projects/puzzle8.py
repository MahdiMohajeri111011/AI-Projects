from algorithms.search import Search

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

    def start_state(self):
        return self.start

    def is_goal(self, state):
        return state == GOAL

    def neighbors(self, state):
        zero = state.index(0)
        row , column = divmod(zero , 3)
        result = []

        for move , (dr , dc) in MOVE.items():
            new_row , new_column = row + dr , column + dc
            if 0 <= new_row < 3 and 0 <= new_column < 3 :
                new_zero = new_row * 3 + new_column
                new = list(state)

                new[zero] , new[new_zero] = new[new_zero] , new[zero]
                result.append((move , tuple(new)))

        return result

    def key(self, state):
        return tuple(state)



#---------------TESTS----------------
def show(path, explored, name):
    if path is None:
        print(f"{name:4} | حل نشد | explored={explored}")
    else:
        print(f"{name:4} | طول={len(path):3} | مسیر={path:20} | explored={explored}")

test = (1, 2, 3,
         4, 0, 5,
         7, 8, 6)

test1 = (1, 2, 3, 4, 0, 5, 6, 7, 8)
test2 = (1, 2, 3, 0, 4, 5, 6, 7, 8)
test3 = (1, 2, 3, 4, 5, 6, 8, 7, 0)

problem = Puzzle8(test)
path, explored = Search.bfs(problem)
if path is None:
    print(f"حل نشد | explored={explored}")
else:
    print(f"طول={len(path)} | {path} | explored={explored}")
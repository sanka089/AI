import heapq

class Node:
    def __init__(self, state, level, heuristic):
        self.state = state
        self.level = level
        self.heuristic = heuristic
    def __lt__(self, other):
        return self.heuristic < other.heuristic
def generate_child(node):
    x, y = find_blank(node.state)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    children = []
    for move in moves:
        child_state = move_blank(node.state, (x, y), move)
        if child_state is not None:
            h = calculate_heuristic(child_state)
            child_node = Node(child_state, node.level + 1, h)
            children.append(child_node)

    return children
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def move_blank(state, src, dest):
    x1, y1 = src
    x2, y2 = dest

    if 0 <= x2 < 3 and 0 <= y2 < 3:
        new_state = [row[:] for row in state]
        new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
        return new_state
    else:
        return None
def calculate_heuristic(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j] and state[i][j] != 0:
                h += 1
    return h
def best_first_search(initial_state):
    start_node = Node(initial_state, 0, calculate_heuristic(initial_state))
    open_list = [start_node]
    closed_set = set()
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return current_node
        closed_set.add(tuple(map(tuple, current_node.state)))
        for child in generate_child(current_node):
            if tuple(map(tuple, child.state)) not in closed_set:
                heapq.heappush(open_list, child)
    return None
initial_state = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
solution_node = best_first_search(initial_state)
if solution_node:
    print("Solution found in", solution_node.level, "moves.")
    print("Path:")
    for row in solution_node.state:
        print(row)
else:
    print("No solution found.")

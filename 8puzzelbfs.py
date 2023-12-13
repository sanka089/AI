import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=""):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = self.calculate_cost()

    def __lt__(self, other):
        return self.cost < other.cost

    def calculate_cost(self):
        cost = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    goal_row, goal_col = divmod(self.board[i][j] - 1, 3)
                    cost += abs(i - goal_row) + abs(j - goal_col)
        return cost

    def get_successors(self):
        successors = []
        zero_i, zero_j = self.find_zero()
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Possible moves: right, down, left, up

        for move in moves:
            new_i, new_j = zero_i + move[0], zero_j + move[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = [row[:] for row in self.board]
                new_board[zero_i][zero_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[zero_i][zero_j]
                successors.append(PuzzleState(new_board, self, move))

        return successors

    def find_zero(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def is_goal(self):
        return self.cost == 0

    def get_solution_path(self):
        path = []
        current = self
        while current:
            path.append((current.move, current.board))
            current = current.parent
        return reversed(path)

def best_first_search(initial_state):
    open_set = []
    closed_set = set()

    heapq.heappush(open_set, initial_state)

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state.get_solution_path()

        closed_set.add(tuple(map(tuple, current_state.board)))

        for successor in current_state.get_successors():
            if tuple(map(tuple, successor.board)) not in closed_set:
                heapq.heappush(open_set, successor)

if __name__ == "__main__":
    initial_board = [
        [1, 2, 3],
        [4, 0, 5],
        [6, 7, 8]
    ]

    initial_state = PuzzleState(initial_board)

    solution_path = best_first_search(initial_state)

    for step, board in solution_path:
        print(f"Move: {step}")
        for row in board:
            print(row)
        print()

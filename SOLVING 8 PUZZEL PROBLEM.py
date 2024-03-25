import heapq

# Define the goal state
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Define the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to find the index of the empty tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None

# Function to calculate the Manhattan distance heuristic
def calculate_heuristic(state):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 3)
                heuristic += abs(row - i) + abs(col - j)
    return heuristic

# Function to generate possible next states
def generate_states(state):
    blank = find_blank(state)
    if blank is None:
        return []
    blank_i, blank_j = blank
    next_states = []
    for move in moves:
        new_i, new_j = blank_i + move[0], blank_j + move[1]
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            next_states.append(new_state)
    return next_states

# Function to perform A* search
def solve_puzzle(start_state):
    visited = set()
    queue = []
    heapq.heappush(queue, (0, start_state, 0))
    while queue:
        _, state, steps = heapq.heappop(queue)
        if state == goal_state:
            return steps
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))
        heuristic = calculate_heuristic(state)
        for next_state in generate_states(state):
            if tuple(map(tuple, next_state)) not in visited:
                next_steps = steps + 1
                heapq.heappush(queue, (next_steps + heuristic, next_state, next_steps))
    return -1

# Function to print the state of the puzzle
def print_puzzle(state):
    for row in state:
        print(" ".join(map(str, row)))

# Function to get user input for the initial state of the puzzle
def get_user_input():
    print("Enter the initial state of the 8-puzzle (use 0 to represent the blank space):")
    initial_state = []
    for i in range(3):
        row = input(f"Enter row {i + 1}: ").split()
        row = [int(num) for num in row]
        initial_state.append(row)
    return initial_state

# Example usage
start_state = get_user_input()

print("\nInitial state of the puzzle:")
print_puzzle(start_state)

steps = solve_puzzle(start_state)
if steps != -1:
    print("\nMinimum number of steps to reach the goal state:", steps)
else:
    print("No solution found.")

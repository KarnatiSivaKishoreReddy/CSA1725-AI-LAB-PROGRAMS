from collections import deque

# Represents the state of the problem
class State:
    def __init__(self, missionaries_left, cannibals_left, boat, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat = boat
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right

    # Check if this state is a goal state
    def is_goal(self):
        return self.missionaries_left == 0 and self.cannibals_left == 0

    # Check if this state is valid
    def is_valid(self):
        if self.missionaries_left >= 0 and self.missionaries_right >= 0 \
           and self.cannibals_left >= 0 and self.cannibals_right >= 0 \
           and (self.missionaries_left == 0 or self.missionaries_left >= self.cannibals_left) \
           and (self.missionaries_right == 0 or self.missionaries_right >= self.cannibals_right):
            return True
        return False

    # String representation of the state
    def __str__(self):
        return "Missionaries on left: {}\nCannibals on left: {}\nBoat: {}\nMissionaries on right: {}\nCannibals on right: {}\n".format(
            self.missionaries_left, self.cannibals_left, '←' if self.boat == 0 else '→', self.missionaries_right, self.cannibals_right)

# Breadth First Search
def breadth_first_search():
    # Initialize starting state
    start_state = State(3, 3, 1, 0, 0)
    if start_state.is_goal():
        return start_state

    # Create queue and visited set
    queue = deque([start_state])
    visited = set()
    visited.add(start_state)

    # BFS
    while queue:
        state = queue.popleft()

        # Generate next possible valid states
        for next_state in generate_next_states(state):
            if next_state not in visited:
                if next_state.is_goal():
                    return next_state
                queue.append(next_state)
                visited.add(next_state)

    return None

# Generate next possible valid states
def generate_next_states(state):
    next_states = []
    if state.boat == 1:  # Boat is on the left bank
        # One missionary crosses left to right
        next_states.append(State(state.missionaries_left - 1, state.cannibals_left,
                                 0, state.missionaries_right + 1, state.cannibals_right))
        # One cannibal crosses left to right
        next_states.append(State(state.missionaries_left, state.cannibals_left - 1,
                                 0, state.missionaries_right, state.cannibals_right + 1))
        # One missionary and one cannibal cross left to right
        next_states.append(State(state.missionaries_left - 1, state.cannibals_left - 1,
                                 0, state.missionaries_right + 1, state.cannibals_right + 1))
        # Two missionaries cross left to right
        next_states.append(State(state.missionaries_left - 2, state.cannibals_left,
                                 0, state.missionaries_right + 2, state.cannibals_right))
        # Two cannibals cross left to right
        next_states.append(State(state.missionaries_left, state.cannibals_left - 2,
                                 0, state.missionaries_right, state.cannibals_right + 2))
    else:  # Boat is on the right bank
        # One missionary crosses right to left
        next_states.append(State(state.missionaries_left + 1, state.cannibals_left,
                                 1, state.missionaries_right - 1, state.cannibals_right))
        # One cannibal crosses right to left
        next_states.append(State(state.missionaries_left, state.cannibals_left + 1,
                                 1, state.missionaries_right, state.cannibals_right - 1))
        # One missionary and one cannibal cross right to left
        next_states.append(State(state.missionaries_left + 1, state.cannibals_left + 1,
                                 1, state.missionaries_right - 1, state.cannibals_right - 1))
        # Two missionaries cross right to left
        next_states.append(State(state.missionaries_left + 2, state.cannibals_left,
                                 1, state.missionaries_right - 2, state.cannibals_right))
        # Two cannibals cross right to left
        next_states.append(State(state.missionaries_left, state.cannibals_left + 2,
                                 1, state.missionaries_right, state.cannibals_right - 2))
    return [state for state in next_states if state.is_valid()]

# Main function
def main():
    solution = breadth_first_search()
    if solution:
        print("Solution found:")
        print(solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

from collections import deque

# Function to find all possible states from the current state
def get_next_states(current_state, x, y):
    next_states = []
    a, b = current_state

    # Fill jug x
    next_states.append((x, b) if a != x else current_state)

    # Fill jug y
    next_states.append((a, y) if b != y else current_state)

    # Empty jug x
    next_states.append((0, b))

    # Empty jug y
    next_states.append((a, 0))

    # Pour from x to y
    pour_amount = min(a, y - b)
    next_states.append((a - pour_amount, b + pour_amount))

    # Pour from y to x
    pour_amount = min(b, x - a)
    next_states.append((a + pour_amount, b - pour_amount))

    return next_states

# Function to solve the Water Jug Problem
def solve_water_jug(x, y, z):
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        current_state = queue.popleft()
        if current_state == (z, 0) or current_state == (0, z):
            return current_state

        visited.add(current_state)

        for next_state in get_next_states(current_state, x, y):
            if next_state not in visited:
                queue.append(next_state)

    return None

# Main function to take inputs and display the result
def main():
    x = int(input("Enter the capacity of jug x: "))
    y = int(input("Enter the capacity of jug y: "))
    z = int(input("Enter the desired amount of water: "))

    solution = solve_water_jug(x, y, z)
    if solution:
        print("Solution found: ", solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()

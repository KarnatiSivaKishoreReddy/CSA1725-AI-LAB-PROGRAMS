import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # Cost from start node to current node
        self.h = h  # Heuristic cost from current node to goal node
        self.f = self.g + self.h  # Estimated total cost

    def __lt__(self, other):
        return self.f < other.f

def astar_search(start_state, goal_state, heuristic, neighbors):
    start_node = Node(start_state, None, 0, heuristic(start_state, goal_state))
    open_list = [start_node]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.state == goal_state:
            return construct_path(current_node)
        
        closed_set.add(current_node.state)

        for neighbor_state in neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue
            
            g = current_node.g + 1  # Assuming uniform cost between neighboring nodes
            h = heuristic(neighbor_state, goal_state)
            neighbor_node = Node(neighbor_state, current_node, g, h)

            # Check if neighbor is already in the open list
            for node in open_list:
                if node.state == neighbor_state and node.g <= g:
                    break
            else:
                heapq.heappush(open_list, neighbor_node)

    return None

def construct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

# Example heuristic function (Manhattan distance)
def manhattan_distance(state, goal_state):
    x1, y1 = state
    x2, y2 = goal_state
    return abs(x1 - x2) + abs(y1 - y2)

# Example neighbor function (4-connected grid)
def neighbors(state):
    x, y = state
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

# Example usage
start_state = (0, 0)
goal_state = (4, 4)
path = astar_search(start_state, goal_state, manhattan_distance, neighbors)
print("Optimal Path:", path)

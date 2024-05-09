from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([Node(initial_state)])

    while queue:
        current_node = queue.popleft()
        current_state = current_node.state

        if current_state == goal_state:
            return get_path(current_node)

        visited.add(current_state)

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state not in visited:
                neighbor_node = Node(neighbor_state, current_node)
                queue.append(neighbor_node)

    return None

def dfs(initial_state, goal_state):
    visited = set()
    stack = [Node(initial_state)]

    while stack:
        current_node = stack.pop()
        current_state = current_node.state

        if current_state == goal_state:
            return get_path(current_node)

        visited.add(current_state)

        for neighbor_state in get_neighbors(current_state):
            if neighbor_state not in visited:
                neighbor_node = Node(neighbor_state, current_node)
                stack.append(neighbor_node)

    return None

def get_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

def get_neighbors(current_state):
    x, y = current_state
    neighbors = []

    # Assuming movements are possible in four directions: up, down, left, right
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in movements:
        new_x, new_y = x + dx, y + dy
        # Check if the new coordinates are within the bounds of the maze
        if 0 <= new_x < maze_width and 0 <= new_y < maze_height:
            # Check if the cell is not a wall (assuming walls are represented by 0)
            if maze[new_x][new_y] != 0:
                neighbors.append((new_x, new_y))

    return neighbors

# Example usage:
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

maze_width = len(maze[0])
maze_height = len(maze)

initial_state = (0, 0)  # Start position
goal_state = (4, 4)  # Goal position

# Using Breadth-First Search
bfs_path = bfs(initial_state, goal_state)
print("BFS Path:", bfs_path)

# Using Depth-First Search
dfs_path = dfs(initial_state, goal_state)
print("DFS Path:", dfs_path)

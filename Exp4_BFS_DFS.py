from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(graph[node])

graph = {}
num_nodes = int(input("Enter the number of nodes: "))
for _ in range(num_nodes):
    node, neighbors = input("Enter node and its neighbors separated by space: ").split()
    graph[node] = neighbors.split(',')

start_node = input("Enter the starting node: ")
print("DFS:")
dfs(graph, start_node)
print("BFS:")
bfs(graph, start_node)

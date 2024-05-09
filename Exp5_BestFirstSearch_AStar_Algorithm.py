import heapq

def euclidean_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def best_first_search(graph, start, end):
    visited = set()
    pq = [(0, start)]
    
    while pq:
        cost, current_node = heapq.heappop(pq)
        if current_node == end:
            return cost
        
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph[current_node]
            for neighbor, neighbor_cost in neighbors.items():
                heapq.heappush(pq, (neighbor_cost, neighbor))

    return float('inf')  # If no path found
def a_star(graph, start, end):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return g_score[end], list(reversed(path))
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + euclidean_distance(neighbor[0], neighbor[1], end[0], end[1])
                heapq.heappush(open_set, (f_score, neighbor))
    
    return float('inf'), None  # If no path found
# Example usage:
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},  # Example grid with costs
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

start = (0, 0)
end = (1, 1)

print("Best-First Search:")
print("Shortest path cost:", best_first_search(graph, start, end))

print("\nA* Algorithm:")
cost, path = a_star(graph, start, end)
print("Shortest path cost:", cost)
print("Shortest path:", path)

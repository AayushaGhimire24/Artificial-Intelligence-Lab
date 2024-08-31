import heapq

# Define the graph using an adjacency list
adj_list = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['B', 'G'],
    'D': ['C', 'G'],
    'E': ['C', 'F'],
    'F': ['C', 'H'],
    'G': ['F', 'H', 'I'],
    'H': ['E', 'I'],
    'I': ['F']
}

# Define heuristic values for each node
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 0
}

# Define user-defined costs for each edge
edge_costs = {
    'A': {'B': 1, 'C': 4, 'D': 3},
    'B': {'E': 2},
    'C': {'B': 2, 'G': 2},
    'D': {'C': 2, 'G': 1},
    'E': {'C': 3, 'F': 5},
    'F': {'C': 1, 'H': 2},
    'G': {'F': 1, 'H': 3, 'I': 1},
    'H': {'E': 3, 'I': 2},
    'I': {'F': 1}
}

def a_star_search(start, goal):
    # Priority queue for the open set
    open_set = []
    heapq.heappush(open_set, (heuristic[start], start))
    
    # Dictionary to keep track of the cost of the shortest path to each node
    g_cost = {start: 0}
    
    # Dictionary to keep track of the parent of each node for path reconstruction
    parents = {start: None}
    
    while open_set:
        # Get the node with the lowest total estimated cost
        _, current = heapq.heappop(open_set)
        
        # If the goal is reached, reconstruct and return the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]
        
        # Explore neighbors
        for neighbor in adj_list[current]:
            tentative_g_cost = g_cost[current] + edge_costs[current][neighbor]
            
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_set, (f_cost, neighbor))
                parents[neighbor] = current
    
    # If the goal is not reachable, return an empty path
    return []

# Display the adjacency list that is being used
print("Adjacency List:")
for key, value in adj_list.items():
    print(key, ':', value)

# Get user input for the start and goal nodes
start = input("\nEnter the starting vertex: ")
goal = input("Enter the goal vertex: ")

# Perform the A* Search
path = a_star_search(start, goal)

# Display the result
if path:
    print(f"\nPath from {start} to {goal} is:")
    for node in path:
        print(node, ' -> ', end='')
    print('End')
else:
    print(f"\nNo path found from {start} to {goal}")

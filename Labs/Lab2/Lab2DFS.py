# Initialization of stack
stack = []
final_path = []

# Our graph represented in form of adjacency list
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

"""
If status is 1 -> ready state
If status is 2 -> the node is enqueued and is said to be in waiting state
If status is 3 -> the node is dequeued
"""
status = {node: 1 for node in adj_list.keys()}

print("\t----DFS Search Algorithm\t\n")

# Display the adjacency list that is being used.
print("Adjacency List Used: \n")
for key, value in adj_list.items():
    print(key, ':', value)

start = input("\nEnter the starting vertex: ")
dest = input("Enter the ending vertex: ")

# Pushing the first node onto the stack
stack.append(start)
# Setting its status to 2 as it now goes into ready state
status[start] = 2

while stack:
    # Pop the node on the top of stack
    node = stack.pop()
    # Add the popped node to the final list
    final_path.append(node)
    # Set the status of popped node to 3
    status[node] = 3

    # Get the adjacent nodes of the popped node from adjacency list
    adj_nodes = adj_list[node]
    # For each node that is adjacent to the popped node
    for adj_node in adj_nodes:
        # If the node is in ready state or untouched:
        if status[adj_node] == 1:
            # Push that node onto the stack
            stack.append(adj_node)
            # Set the status of that node to waiting (2)
            status[adj_node] = 2

    # If the destination node is reached, exit the loop
    if node == dest:
        break

print(f"\nPath from {start} to {dest} is: \n")
for each in final_path:
    print(each, ' -> ', end='')

# To properly end the path display
print('End')





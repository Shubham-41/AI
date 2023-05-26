# BFS

# first, we will create the graph for which we will use the breadth-first search.
# After creation, we will create two lists, one to store the visited node of the graph
# and another one for storing the nodes in the queue.
# After the above process, we will declare a function with the parameters as visited nodes,
# the graph itself and the node respectively. And inside a function, we will keep appending
# the visited and queue lists.
# Then we will run the while loop for the queue for visiting the nodes and then will remove
# the same node and print it as it is visited.
# At last, we will run the for loop to check the not visited nodes and then append the same
# from the visited and queue list.
# As the driver code, we will call the user to define the bfs function with the
#  first node we wish to visit.
# The time complexity of the Breadth first Search algorithm is in the form of O(V+E),
# where V is the representation of the number of nodes and E is the number of edges.
# Also, the space complexity of the BFS algorithm is O(V)


# Applications :
 # In GPS navigation, it helps in finding the shortest path available from one point to another.
 # In pathfinding algorithms
 # Cycle detection in an undirected graph
 # In minimum spanning tree
 # To build index by search index
 # In Ford-Fulkerson algorithm to find maximum flow in a network.

graph = {
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited = [] # List for visited Nodes
queue = [] # initialize the queue

def bfs (visited,graph,node): #function for BFS
    visited.append(node)
    queue.append(node)

    while queue :# Creating Loop to visit each node
        m = queue.pop(0)
        print(m," ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("Following is the Breadth First Search (Iterative) : ")
bfs(visited,graph,'5')


# Example graph
graph_R = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited_R= []  # List to track visited nodes
queue_R = ['5']  # Initialize the queue with the starting node

def bfs_recursive(graph_R, visited_R, queue_R):
    if not queue_R:  # Base case: If the queue is empty, we have visited all nodes
        return

    node = queue_R.pop(0)  # Get the first node from the queue

    # Process the node
    print(node, end=" ")  # Print the value of the node or perform any other operation

    visited_R.append(node)  # Mark the node as visited

    # Add the unvisited neighbors of the node to the queue
    for neighbor in graph_R[node]:  # Use graph_R instead of graph
        if neighbor not in visited_R and neighbor not in queue_R:
            queue_R.append(neighbor)

    bfs_recursive(graph_R, visited_R, queue_R)  # Recursively call the function with updated queue



print("Following is the Breadth First Search (Recursive):")
bfs_recursive(graph_R, visited_R, queue_R)



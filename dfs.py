
# Algorithm :-

# Start by initializing an empty set visited
# to keep track of the visited vertices,
# and a  stack with the starting vertex.
# While the stack is not empty, you pop a vertex from the stack.
# If the vertex has not been visited, you mark it as visited, print it
# and get its neighbors from the graph.
# Then, you iterate over the neighbors and push them onto the stack
# if they haven't been visited.

# Example graph
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}


def dfs(graph, node):
    visited = []
    stack = [node]

    while stack:
        m = stack.pop()
        print(m, " ")
        visited.append(m)

        for neighours in graph[m]:
            if neighours not in visited:
                visited.append(neighours)
                stack.append(neighours)


print("DFS Implementation Iterrative Approach : ")
dfs(graph, '5')

# Output :-
# DFS Implementation Iterrative Approach :
# A  C   F   B   E   D

# Output :-
# DFS Implementation Iterrative Approach :
# 5   7   8   3   4   2

# Recursive Implementation Of DFS Algorithm :

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []

def dfs_recursive(graph, node, visited):
    visited.append(node)
    print(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)


dfs_recursive(graph, 'A', visited)

# Output :- A B D E F C
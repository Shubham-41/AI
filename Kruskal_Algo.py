# Below are the steps for finding MST using Kruskal’s algorithm 

# Sort all the edges in non-decreasing order of their weight. 
# Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far.
# If cycle is not formed, include this edge. Else, discard it. 
# Repeat step Step 2 until there are (V-1) edges in the spanning tree.
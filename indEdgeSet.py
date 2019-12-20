# Finds the maximum number of edges that don't share a node within a tree graph in O(n) time
# tree - graph adjacency list
# node - subtree root
# Returns array of two values - if edge to subtree root node is picked or not picked
def findEdges(tree, node):
    # If this node is adjacent, then the edge to its parent must be counted
    isAdjacentEdges = 1
    notAdjacentEdges = 0
    isAdjacentChildren = []
    notAdjacentChildren = []

    # Loops through the subtrees children and calls findEdges() in O(n) time
    for child in tree[node]:
        childEdges = findEdges(tree, child)
        # If this node is adjacent, no edge can be used from it to its children,
        # so this subtree would only have the sum of edges
        # from the subtrees of each non-adjacent child
        isAdjacentEdges += childEdges[1]
        # If this node is not adjacent, one of the edges to a child might be used
        # so the subtree would have the edges from the subtree of the adjacent child
        # plus the sum of the edges from the subtrees of the other non-adjacent children
        # To get the calculate maximum value these child subtree edges are stored in two arrays
        isAdjacentChildren.append(childEdges[0])
        notAdjacentChildren.append(childEdges[1])


    # If this node is not adjacent and has children,
    # finds the maximums combination of one adjacent and other non-adjacent children
    # in O(k) time, where k is number of children a node has. k < n
    if (len(tree[node]) > 0):
        for i in range(len(isAdjacentChildren)):
            calc = isAdjacentChildren[i] + sum(notAdjacentChildren) - notAdjacentChildren[i]
            if calc > notAdjacentEdges:
                notAdjacentEdges = calc

    # Return the maximum edge number from this subtree
    return [isAdjacentEdges, notAdjacentEdges]


tree1 = [[1, 2], [3, 4, 5], [6], [7], [8, 9], [], [], [], [], []]
tree2 = [[1, 2, 3], [], [4, 5], [6, 7], [8, 9],[10],[11, 12], [13], [], [], [14], [], [], [15], [], []]
tree3 = [[1, 2], [3, 4], [5, 6, 7], [], [8, 9], [], [10], [], [], [], [11, 12], [], []]

print('Maximum removable edges:', findEdges(tree1, 0)[1])
print('Maximum removable edges:', findEdges(tree2, 0)[1])
print('Maximum removable edges:', findEdges(tree3, 0)[1])
# Maximum removable edges: 4
# Maximum removable edges: 7
# Maximum removable edges: 4

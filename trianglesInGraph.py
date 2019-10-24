# Input adjacency list of graph
adjList = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3],
}

# Creates an empty array an initializes it with 0 in O(n^2)
adjMatrix = [[0 for _ in range(len(adjList))] for _ in range(len(adjList))]

# Creates an adjacency matrix from the adjacency list in O(n+m)
for i in range(0, len(adjList)):
    for j in range(0, len(adjList[i])):
        column = adjList[i][j]
        adjMatrix[i][column] = 1

# Create a list of edges from the adjacency list in O(n+m)
edgeList = []
for i in range(0, len(adjList)):
    for j in range(0, len(adjList[i])):
        edgeList.append([i, adjList[i][j]])

# Traverses edge list and checks in the adjacency matrix
# if edge nodes are connected to a common node in O(n*m)
triangleCount = 0
for i in range(0, len(edgeList)):
    edgeVertexOne = edgeList[i][0]
    edgeVertexTwo = edgeList[i][1]
    for j in range(0, len(adjMatrix)):
        if adjMatrix[j][edgeVertexOne] == 1 and adjMatrix[j][edgeVertexTwo]:
            triangleCount += 1

# Returns 18
print(triangleCount)





for edge in edgeList:
    print(edge)
print()

for i in range(0, len(adjList)):
    print(adjList[i])
print()

for node in adjMatrix:
    print(node)
print()

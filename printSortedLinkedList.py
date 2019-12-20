# Input collection of gems - each an array containing the gem name
# and a "pointer" to the worseThan gem positions
gemList = {
    0: ['A', 2],
    1: ['B', 3],
    2: ['C', 4],
    3: ['D', 0],
    4: ['E', 1],
}

orderedGemList = {}

# Recursive function that loops through all the gems using the worseThan
# pointers and appends the gem to an ordered gem list in O(n) time
def orderCollection(inputGemList, outputGemList, gemPosition, depth = 1):
    if depth < len(inputGemList):
        orderCollection(inputGemList, outputGemList, inputGemList[gemPosition][1], depth + 1)

    outputGemList[depth-1] = inputGemList[gemPosition]

# Calls recursive ordering function
orderCollection(gemList, orderedGemList, 0)

# Prints the gems from the ordered list in a line where each gem has
# a worse gem on the left and a better gem on the right in O(n)
# OUTPUT: GEM-A <-- GEM-C <-- GEM-E <-- GEM-B <-- GEM-D <--
for i in range(0, len(orderedGemList)):
    print("GEM-{} <-- ".format(orderedGemList[i][0]), end = '')


givenSet = [34, 40, 28, 31, 44, 47, 33]
# Possible subsets = [34, 44, 33], [40, 28, 44, 33],
# [28, 44, 33], [31, 44, 33], [44, 33], [47, 33]
# Longest possible subset length = 4

givenSetLength = len(givenSet)

# Array to hold possible subset lengths, initialized with 1
subsetLengths = [1 for i in range(givenSetLength)]

# Loops through the given set
for i in range(givenSetLength):
    # Loops through all of the previous elements
    for j in range(i):
        # If an element from the set fulfills the criteria
        # with another previous element from the set
        # update the possible subset length for this element
        # with the possible subset length for this previous element + 1
        # (if it's greater than the current possible subset length)
        if ((givenSet[i] > givenSet[j] + 10) or (givenSet[i] < givenSet[j] - 10)):
            subsetLengths[i] = max(subsetLengths[i], subsetLengths[j] + 1)

print(max(subsetLengths))
# prints 4















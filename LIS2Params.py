# Binary search in O(log n) to find the next largest end element
# of a sequence after the current element
def findNextEndEleement(sequence, lastElements, high, elem):
    low = 0
    while (high - low > 1):
        mid = (high + low) // 2
        if (sequence[lastElements[mid]][0] >= elem[0] and\
                sequence[lastElements[mid]][1] >= elem[1]):
            high = mid
        else:
            low = mid

    # Check if the previous largest end element is smaller than the current element
    # and the sequence would still be true if the current element replaces the found element
    if (sequence[lastElements[high - 1]][0] < elem[0] and\
            sequence[lastElements[high - 1]][1] < elem[1]):
        return high
    else:
        return None


# Finds longest increasing subsequence in an array in O(n log n) by
# looping through tha array in O(n) and using binary search in (log n)
def findLIS(sequence):
    n = len(sequence)

    # Array to hold the position of the last element
    # of a subsequence of a particular length
    # Position in array corresponds to the length of the subsequence
    # Initialized with 0 in O(n)
    lastElements = [0 for i in range(n + 1)]

    # Array to hold links between the positions of the last and previous elements
    # of a sequence. Initialized with None in O(n)
    elementLinks = [None for i in range(n + 1)]

    # Length of the longest subsequence
    length = 1
    # Loops through the elements in O(n)
    for i in range(1, n):
        # If the current element is smaller than the first element of a subsequence of length 1
        # Replace it with the current element
        if (sequence[i][0] <= sequence[lastElements[0]][0] and\
                sequence[i][1] <= sequence[lastElements[0]][1]):
            # Replace first element
            lastElements[0] = i

        # If the current element is larger than the last element of the longest subsequence
        # Create a new subsequence with it as the last element
        elif (sequence[i][0] > sequence[lastElements[length - 1]][0] and\
              sequence[i][1] > sequence[lastElements[length - 1]][1]):
            # Creates new link for new last element
            elementLinks[i] = lastElements[length - 1]
            # Creates new subsequence
            lastElements[length] = i
            length += 1

        # If the current element is between the first element of a subsequence
        # and the last element of the longest subsequence
        # use binary search to find the next largest end element of a sequence after the current element
        # in O(log n) and, if search doesn't return None, replace it with the current element
        else:
            pos = findNextEndEleement(sequence, lastElements, length - 1, sequence[i])
            if (pos != None):
                # Update links
                elementLinks[i] = lastElements[pos - 1]
                # Update last element of subsequence
                lastElements[pos] = i

    # Creates LIS array - Initialized with 0 in O(n)
    # then fills it with the last element of the longest sequence
    # plus each of the sequences previous element in O(n)
    lis = [0 for i in range(length)]
    i = lastElements[length - 1]
    j = length
    while (i is not None):
        lis[j - 1] = sequence[i]
        i = elementLinks[i]
        j -=1
    return lis


arrayOfStamps = [[4, 3], [4, 2], [4, 2], [5, 3], [5, 2], [2, 2],\
                 [6, 4], [3, 2], [3, 3], [5, 7], [4, 5], [5, 7]]

lis = findLIS(arrayOfStamps)
print("LIS -", lis)
print("Length -", len(lis))
#LIS - [[2, 2], [3, 3], [4, 5], [5, 7]]
# Length - 4

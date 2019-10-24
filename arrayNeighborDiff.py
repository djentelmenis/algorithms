# Input unsorted array of integers
inputArray = [3, 12, 7, 23, 4, 20]

# Creates and initializes array with 0
# in time equal to biggest input array value
valueArray = [0] * (max(inputArray) + 1)

# Loops through the input array and populates the value array in O(n)
for i in range(0, len(inputArray)):
    if valueArray[inputArray[i]] == 0:
        valueArray[inputArray[i]] = inputArray[i]

# Loops through the value array and calculates the biggest difference
# between two values in time equal to biggest input array value
bigDiff = 0
prevNum = 0
for i in range(0, len(valueArray)):
    if valueArray[i] != 0:
        if valueArray[i] - prevNum > bigDiff:
            bigDiff = valueArray[i] - prevNum
        prevNum = valueArray[i]

# Returns 8
print(bigDiff)

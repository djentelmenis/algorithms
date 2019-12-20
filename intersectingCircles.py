# Merge sort, that can sort objects by their elements in O(n log n)
# Original code by Mayank Khanna
def mergeSort(arr, sortBy):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L, sortBy)  # Sorting the first half
        mergeSort(R, sortBy)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # print(L[i][1], R[j][1])
            if L[i][sortBy] < R[j][sortBy]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Detects whether 2 circles are intersecting in const time
def isInterseting(firstCircle, secondCircle):
    x1 = firstCircle[0]
    y1 = firstCircle[1]
    r1 = firstCircle[2]
    x2 = secondCircle[0]
    y2 = secondCircle[1]
    r2 = secondCircle[2]
    distanceSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radiusSumSq = (r1 + r2) * (r1 + r2)
    if (distanceSq <= radiusSumSq):
        return True
    else:
        return False


# Detects how many circles are intersecting in array of circles
# in O(n * k) time
# k - highest number of projected circles intersecting on x axis
def detectIntersections(circles):
    numberOfCircles = len(circles)
    intersectingCircles = 0
    for i in range(numberOfCircles - 1):
        if circles[i][4] > circles[i + 1][3]:
            j = 1
            while circles[i][4] >= circles[i + j][3] and i + j < numberOfCircles - 1:
                if isInterseting(circles[i], circles[i + j]):
                    intersectingCircles += 1
                j += 1
        i += 1
    return intersectingCircles


# Creates a single array in O(n) where each element is a
# circle object with x, y, r, x-r and x+y, sorted by x-r
def createSortedCircles(arrayOfCircles, arrayOfPoints):
    arrayOfPointCircles = []
    for i, point in enumerate(arrayOfPoints):
        pointCircle = point
        radius = arrayOfCircles[i]
        pointCircle.append(radius)
        pointCircle.append(point[0] - radius)
        pointCircle.append(point[0] + radius)
        arrayOfPointCircles.append(pointCircle)
    mergeSort(arrayOfPointCircles, 3)
    return arrayOfPointCircles


arrayOfCircles = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 6]
arrayOfPoints = [[12, 11], [32, 8], [4, 15.5], [8, 35], [10, 6], [7, 9], \
                 [15, 15], [35, 15], [42, 7], [30, 18], [20, 10]]

sortedCircles = createSortedCircles(arrayOfCircles, arrayOfPoints)
print("Sorted circle array\n", sortedCircles)
print('Intersections found:', detectIntersections(sortedCircles))
# Intersections found: 3

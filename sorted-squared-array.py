array = [-1,-2,-3]

# O(NlogN) time -- to sort
# O(N) space -- extra array before sorting
# def sortedSquaredArray(array):
#     squared = [x**2 for x in array]
#     squared.sort()
#     return squared


# O(N) time -- traversal
# O(N) space -- array of squared values
def sortedSquaredArray(array):
    left = 0
    right = len(array) - 1
    sorted = []
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            sorted.insert(0,array[right]**2)
            right -= 1
        else:
            sorted.insert(0,array[left]**2)
            left += 1 

    return sorted


print(sortedSquaredArray(array))


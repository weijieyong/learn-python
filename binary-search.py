# Write a function that takes in a sorted array of integers as well as a target integer. The
# function should use the Binary Search algorithm to determine if the target integer is
# contained in the array and should return its index if it is, otherwise -1
#---------------------------------------------------------------------
array = [0, 1, 21, 33, 45, 61]
target = 61

#first try
# def binarySearch(array, target):
#     leftIdx = 0
#     rightIdx = len(array) - 1
#     midIdx = round((rightIdx + leftIdx)/2)
#     while leftIdx < rightIdx:
#         if target == array[midIdx]:
#             return midIdx
#         elif target == array[leftIdx]:
#             return leftIdx
#         elif target == array[rightIdx]:
#             return rightIdx
#         elif target < array[midIdx]:
#             rightIdx = midIdx - 1
#             midIdx = round((rightIdx + leftIdx)/2)
#         else:
#             leftIdx = midIdx + 1 
#             midIdx = round((rightIdx + leftIdx)/2)
#     return -1


#refined
def binarySearch(array, target):
    leftIdx = 0
    rightIdx = len(array) - 1
    while leftIdx < rightIdx:
        midIdx = (rightIdx + leftIdx) // 2
        if target == array[midIdx]:
            return midIdx
        elif target == array[leftIdx]:
            return leftIdx
        elif target == array[rightIdx]:
            return rightIdx
        elif target < array[midIdx]:
            rightIdx = midIdx - 1
        else:
            leftIdx = midIdx + 1 
    return -1

print(binarySearch(array, target))

# Algo's explaination
# iterative solution: run in O(Log(N)) time | O(1) space
# recursive solution: run in O(Log(N)) time | O(Log(N)) space


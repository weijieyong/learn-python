# bubble sort
import time

start = time.time()
array = [8, 5, 2, 9, 5, 6, 3]

def bubbleSort(array):
    for last in range(len(array)-1, 0, -1):
        swapsCount = 0
        for i in range(last):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapsCount += 1
        if swapsCount == 0:
            break
    
    return array

#######################
# algo's solutions
#######################
# def bubbleSort(array):
#     isSorted = False
#     counter = 0
#     while not isSorted:
#         isSorted = True
#         for i in range(len(array)-1-counter):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#                 isSorted = False
#         counter += 1
#     return array

timeTaken = time.time() - start

print(bubbleSort(array))
print("time taken: ", timeTaken)

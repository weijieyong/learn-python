#%%
def insertionSort(array):
    for i in range(1,len(array)):
        for j in range(i, 0, -1):
            while array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
        
    return array

array = [8, 5, 2, 9, 5, 6, 3]
print(insertionSort(array))

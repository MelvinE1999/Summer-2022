# random pivot index
from random import randint


def partition(arr, lo, hi):
    pivotIndex = randint(0, ((hi - lo) + 1 + lo))

    arr[hi], arr[pivotIndex] = arr[pivotIndex], arr[hi]
    pivot = arr[hi]

    i = lo - 1
    for j in range(lo,hi):
        if arr[j] < pivot:
            arr[j],arr[i+1] = arr[i+1],arr[j]
            i += 1
    
    arr[hi], arr[i+1] = arr[i+1],arr[hi]

    return i+1
    

def quicksort(arr, lo, hi):
    if lo >= hi:
        return 

    pivot = partition(arr,lo,hi)
    quicksort(arr, lo, pivot - 1)
    quicksort(arr, pivot + 1, hi)

# methods to generate data are based off an assignment from CSC 140
# start
def generateSortedData():
    data = [0] * size

    for i in range(size):
        data[i] = i * 3 + 5
    return data

def generateNearlySortedData():
    data = generateSortedData()

    for i in range(size):
        if i % 10 == 0:
            if i + 1 < size:
                data[i] = data[i + 1] + 7
    return data

def generateReverselySortedData():
    data = [0] * size

    for i in range(size):
        data[i] = (size - i) * 2 + 3
    return data

def generateRandomData():
    data = [0] * size

    for i in range(size):
        data[i] = randint(1,10000000)
    return data
# end

def tester():
    arr_sorted = generateSortedData()
    arr_near_sorted = generateNearlySortedData()
    arr_reverse_sorted = generateReverselySortedData()
    arr_rand = generateRandomData()

    assert quicksort(arr_sorted, 0, size-1) == arr_sorted.sort()
    assert quicksort(arr_near_sorted, 0, size-1) == arr_near_sorted.sort()
    assert quicksort(arr_reverse_sorted, 0, size-1) == arr_reverse_sorted.sort()
    assert quicksort(arr_rand, 0, size-1) == arr_rand.sort()




if __name__ == "__main__":
    size = 10000
    tester()
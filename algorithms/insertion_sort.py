from random import randint

# input: an array of numbered elements
# output: a sorted array
def insertionSort(arr): # theta(n^2)
    n = len(arr)
    for i in range(1, n): # theta(n)
        key = arr[i]
        j = i - 1
        for i in range(j, -1, -1): # theta(n)
            if arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                break
        arr[j + 1] = key

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

    assert insertionSort(arr_sorted) == arr_sorted.sort()
    assert insertionSort(arr_near_sorted) == arr_near_sorted.sort()
    assert insertionSort(arr_reverse_sorted) == arr_reverse_sorted.sort()
    assert insertionSort(arr_rand) == arr_rand.sort()




if __name__ == "__main__":
    size = 10000
    tester()
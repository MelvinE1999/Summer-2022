from random import randint

def merge(arr, lo, mid,hi):
    max_ele = max(arr) + 1
    l_arr = list(arr[:mid])
    l_arr.append(max_ele)
    r_arr = list(arr[mid:])
    r_arr.append(max_ele)

    i = 0
    j = 0
    for k in range(lo,hi+1):
        if l_arr[i] < r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1

def mergeSort(arr, lo, hi):
    if lo == hi:
        return
    
    mid = (lo + hi) //2
    mergeSort(arr,lo,mid)
    mergeSort(arr,mid + 1, hi)
    merge(arr,lo,mid,hi)

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

    assert mergeSort(arr_sorted, 0, size-1) == arr_sorted.sort()
    assert mergeSort(arr_near_sorted, 0, size-1) == arr_near_sorted.sort()
    assert mergeSort(arr_reverse_sorted, 0, size-1) == arr_reverse_sorted.sort()
    assert mergeSort(arr_rand, 0, size-1) == arr_rand.sort()




if __name__ == "__main__":
    size = 10000
    tester()
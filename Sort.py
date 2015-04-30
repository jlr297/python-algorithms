import random
'''
Sorting algorithms for lists
'''
def shuffle(items):
    for x in range(len(items)):
        rand1 = random.randint(0,len(items)-1) 
        rand2 = random.randint(0,len(items)-1)
        swap(items, rand1, rand2)

def swap(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp

def bubbleSort(items):
    numSwaps = 0
    madeSwap = True
    while madeSwap:
        madeSwap = False
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                swap(items, i, i+1)
                madeSwap = True
                numSwaps += 1
    return numSwaps

def selectionSort(items):
    numSwaps = 0
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            swap(items, i, min_index)
            numSwaps += 1
    return numSwaps

def insertionSort(items):
    numSwaps = 0
    for i in range(0, len(items)):
        for j in range(i, 0, -1):
            if items[j-1] <= items[j]:
                break
            swap(items, j, j-1)
            numSwaps += 1
    return numSwaps

def mergeSort(items):
    if len(items) <= 1:
        return items
    
    left = items[:len(items)/2]
    right = items[len(items)/2:]
    
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)    

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
            if left == None:
                break
        else:
            result.append(right[0])
            right = right[1:]
            if right == None:
                break
    for x in left:
        result.append(x)
    for y in right:
        result.append(y)
    return result

def heapsort(items):
    heapify(items)
    end = len(items) - 1
    while end > 0:
        swap(items, 0,  end)
        end -= 1
        siftdown(items, 0, end)

def heapify(items):
    start = (len(items)-2)/2
    while start >= 0:
        siftdown(items, start, len(items)-1)
        start -= 1

def siftdown(items, start, end):
    root = start
    while (root*2 + 1) <= end:
        child = (root*2) + 1
        swap_index = root
        if items[swap_index] < items[child]:
            swap_index = child
        if child+1 <= end and items[swap_index] < items[child+1]:
            swap_index = child + 1
        if swap_index == root:
            return
        else:
            swap(items, root, swap_index)
            root = swap_index

def quicksort(items, low, hi):
    if low < hi:
        p = partition(items, low, hi)
        quicksort(items, low, p-1)
        quicksort(items, p+1, hi)

def partition(items, low, hi):
    pivotIndex = low + (hi-low)/2
    pivotValue = items[pivotIndex]
    swap(items, pivotIndex, hi)
    storeIndex = low
    for i in range(low, hi):
        if items[i] <= pivotValue:
            swap(items, i, storeIndex)
            storeIndex += 1
    swap(items, storeIndex, hi)
    return storeIndex

def bogosort(items):
    while not is_sorted(items):
        shuffle(items)

def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

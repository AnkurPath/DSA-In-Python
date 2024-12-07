import heapq


def k_smallest(arr,k):
    n = len(arr)
    heap = arr[:k]
    heapq._heapify_max(heap)

    for i in range(k,n):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap,arr[i])

    return heap

arr = [2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6]

k = 4

elements = k_smallest(arr,k)
for element in elements:
    print(element,end="")
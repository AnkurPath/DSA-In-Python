import heapq

def kth_largest_element(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num) # add current element to the heap
        print(min_heap)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

        print(min_heap)

    return min_heap[0]





arr = [3, 2, 5, 1, 4]
k =2

print(kth_largest_element(arr, k))
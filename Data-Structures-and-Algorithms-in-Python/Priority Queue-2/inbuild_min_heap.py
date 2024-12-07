import heapq

li = [1, 5, 4, 8, 7, 9, 11]
heapq.heapify(li)
print(li)            # [1, 5, 4, 8, 7, 9, 11]

# Push a new element
heapq.heappush(li,2)
print(li)            # [1, 2, 4, 5, 7, 9, 11, 8]

# Remove min ele 
heapq.heappop(li)
print(li)            # [2, 5, 4, 8, 7, 9, 11]

# replace min element with passed value and restructure it
heapq.heapreplace(li,6)
print(li)            # [4, 5, 6, 8, 7, 9, 11]



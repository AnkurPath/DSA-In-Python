import heapq

li = [1, 5, 4, 8, 7, 9, 11]
heapq.heapify(li)
print(li)

# Push a new element
heapq.heappush(li,2)
print(li)

# Remove min ele 
heapq.heappop(li)
print(li)

# replace min element with passed value and restructure it
heapq.heapreplace(li,6)
print(li)



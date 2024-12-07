import heapq

"""
Refer this 
https://github.com/python/cpython/blob/main/Lib/heapq.py
"""

li = [1, 5, 4, 7, 8, 9, 2, 3]
heapq._heapify_max(li)
print(li)               # [9, 8, 4, 7, 5, 1, 2, 3]

heapq._heappop_max(li)
print(li)              # [8, 7, 4, 3, 5, 1, 2]


heapq._heapreplace_max(li,0)
print(li)              # [7, 5, 4, 3, 0, 1, 2]

# for inserting new elememt

li.append(6)

heapq._siftdown_max(li,0,len(li) - 1)
print(li)              # [7, 6, 4, 5, 0, 1, 2, 3]
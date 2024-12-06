# Problem statement
# Given an integer array of size N. Sort this array (in decreasing order) using heap sort.

# Note: Space complexity should be O(1).

# Detailed explanation ( Input/output format, Notes, Images )
# Input Format:
# The first line of input contains an integer, that denotes the value of the size of the array or N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output Format :
# The first and only line of output contains array elements after sorting. The elements of the array in the output are separated by single space.

# Constraints :
# 1 <= n <= 10^6
# Time Limit: 1 sec
# Sample Input 1:
# 6 
# 2 6 8 5 4 3
# Sample Output 1:
# 8 6 5 4 3 2

# we have to create heap
def down_heapify(arr, i, n):
    parent_index = i
    left_child_index = 2 * parent_index + 1
    right_child_index = 2 * parent_index + 2

    while left_child_index < n :
        min_index = parent_index

        if arr[min_index] > arr[left_child_index]:
            min_index = left_child_index
        
        if right_child_index < n and arr[min_index] > arr[right_child_index]:
            min_index = right_child_index

        if min_index == parent_index:
            return

        arr[parent_index], arr[min_index] = arr[min_index], arr[parent_index]

        parent_index = min_index
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

    return

def heap_sort(arr):
    n = len(arr)
    
    # Build the Heap
    for i in range(n // 2 - 1, -1, -1):
        down_heapify(arr, i,n)

    # Removing n element from Heap and Putting them into correct position
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heapify(arr,0,i)
    return


# Input handling
n = int(input())  # Read the size of the array (this is expected in the problem statement)
arr = list(map(int, input().split()))  # Read the array elements

heap_sort(arr)

# Output the sorted array in descending order
for ele in arr:
    print(ele, end=" ")

 
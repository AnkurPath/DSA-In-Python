from sys import stdin
import heapq

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        newNode = LinkedListNode(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.head is None

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

def buyTicket(arr, n, k):
    # Initialize the queue with (index, priority)
    queue = Queue()
    for i in range(n):
        queue.enqueue((i, arr[i]))

    # Max-heap to track the highest priorities
    max_heap = [-p for p in arr]
    heapq.heapify(max_heap)

    time = 0
    while not queue.isEmpty():
        idx, priority = queue.dequeue()

        # Check if this person has the highest priority
        if priority == -max_heap[0]:
            time += 1
            heapq.heappop(max_heap)  # Remove the highest priority from heap
            if idx == k:  # If this is the person we are tracking
                return time
        else:
            # Add the person back to the end of the queue
            queue.enqueue((idx, priority))

    return time

# Taking input using fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return n, [], int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

# Main
n, arr, k = takeInput()
print(buyTicket(arr, n, k))



# Here's a detailed explanation of the code:

# ---

# ### 1. **Classes:**
# #### **`LinkedListNode` Class**
# This class defines a node in a singly linked list:
# - **Attributes**:
#   - `data`: Stores the value of the node.
#   - `next`: A pointer to the next node in the list.
# - Used in the `Queue` class to represent each person in the queue.

# #### **`Queue` Class**
# This is a custom implementation of a queue using a linked list:
# - **Attributes**:
#   - `head`: Points to the first node in the queue.
#   - `tail`: Points to the last node in the queue.
#   - `size`: Tracks the number of elements in the queue.
# - **Methods**:
#   - `enqueue(data)`: Adds a new element at the end of the queue.
#   - `dequeue()`: Removes and returns the front element of the queue.
#   - `getSize()`: Returns the current size of the queue.
#   - `isEmpty()`: Returns `True` if the queue is empty, otherwise `False`.
#   - `peek()`: Returns the front element of the queue without removing it.

# The `Queue` is used to simulate the line of people waiting for tickets.

# ---

# ### 2. **`buyTicket` Function**
# This is the main function that simulates the ticket-buying process.

# #### **Input**:
# - `arr`: A list of integers representing the priorities of people in the queue.
# - `n`: Number of people in the queue.
# - `k`: The index of the person whose time to get the ticket we need to find.

# #### **Output**:
# - Returns the time (in seconds) it takes for the person at index `k` to get the ticket.

# ---

# #### **Logic**:
# 1. **Initialize the Queue**:
#    - Use the `Queue` class to represent the queue of people, where each person is represented as a tuple `(index, priority)`.
#    - This allows us to track both their priority and their original position.

# 2. **Create a Max-Heap for Priorities**:
#    - Use Python's `heapq` module to create a max-heap.
#    - Since `heapq` only supports min-heaps, priorities are stored as negative values so that the largest priority is at the top.

# 3. **Simulate Ticket Buying**:
#    - While the queue is not empty:
#      - Dequeue the first person in the queue.
#      - Check if their priority matches the highest priority in the max-heap:
#        - **If yes**:
#          - Increment `time` (as giving a ticket takes 1 second).
#          - Remove the highest priority from the heap.
#          - Check if this person is the one we're tracking (index `k`). If yes, return the elapsed `time`.
#        - **If no**:
#          - Re-enqueue the person at the end of the queue.

# 4. **Output the Time**:
#    - When the person at index `k` gets the ticket, return the total time elapsed.

# ---

# ### 3. **Input Handling:**
# - The `takeInput` function reads input data using `stdin`:
#   - Reads `n` (number of people).
#   - Reads the list `arr` of size `n` (priorities).
#   - Reads the index `k` of the person whose ticket time is to be calculated.
# - Returns `n`, `arr`, and `k` to the main function.

# ---

# ### Example Execution:

# #### Input:
# ```plaintext
# 5
# 2 3 2 2 4
# 3
# ```

# #### Step-by-Step Execution:
# 1. **Initialize**:
#    - `queue`: `[(0, 2), (1, 3), (2, 2), (3, 2), (4, 4)]`
#    - `max_heap`: `[-4, -3, -2, -2, -2]`

# 2. **Simulate the Process**:
#    - **Time = 0**:
#      - Dequeue `(0, 2)`:
#        - Priority `2` < Max `4`.
#        - Re-enqueue `(0, 2)`.
#    - **Time = 0**:
#      - Dequeue `(1, 3)`:
#        - Priority `3` < Max `4`.
#        - Re-enqueue `(1, 3)`.
#    - **Time = 1**:
#      - Dequeue `(4, 4)`:
#        - Priority `4` == Max `4`.
#        - Give ticket, pop `4` from heap.
#    - **Time = 2**:
#      - Dequeue `(0, 2)`:
#        - Priority `2` < Max `3`.
#        - Re-enqueue `(0, 2)`.
#    - **Time = 3**:
#      - Dequeue `(1, 3)`:
#        - Priority `3` == Max `3`.
#        - Give ticket, pop `3` from heap.
#    - **Time = 4**:
#      - Dequeue `(3, 2)` (our target person):
#        - Priority `2` == Max `2`.
#        - Give ticket.

# 3. **Result**:
#    - Total time = `4`.

# ---

# ### Complexity:
# 1. **Time Complexity**:
#    - Queue operations (`enqueue` and `dequeue`) are \( O(1) \).
#    - Max-heap operations (`heappop`, `heappush`) are \( O(\log n) \).
#    - Total complexity is \( O(n \log n) \).

# 2. **Space Complexity**:
#    - Queue stores \( n \) elements: \( O(n) \).
#    - Max-heap stores \( n \) elements: \( O(n) \).
#    - Total space complexity: \( O(n) \).

# ---

# ### Summary:
# This code simulates a ticket-buying process where priorities dictate the order. The custom `Queue` handles the queue operations, and the max-heap ensures efficient priority comparison. The logic accurately computes the time for a specific person to get the ticket.

# 2239
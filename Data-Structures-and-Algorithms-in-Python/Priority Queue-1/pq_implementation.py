class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def get_size(self):
        return len(self.pq)
    
    def is_empty(self):
        return self.get_size == 0
    
    def get_min(self):
        if self.is_empty:
            return None
        return self.pq[0].value
    
    def __percolate_up(self):
        child_index = self.get_size() - 1
        while child_index > 0:
            parent_index = (child_index -1) // 2
            if self.pq[child_index].priority < self.pq[parent_index].priority:
                self.pq[child_index],self.pq[parent_index] = self.pq[parent_index],self.pq[child_index]
                child_index = parent_index
            else:
                break

    def insert(self,value,priority):
        pq_node = PriorityQueueNode(value,priority)
        self.pq.append(pq_node)
        self.__percolate_up()

    def __percolate_down(self):
        parent_index = 0
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        while left_child_index < self.get_size():
            min_index = parent_index
            if self.pq[min_index].priority > self.pq[left_child_index].priority:
                min_index = left_child_index

            if right_child_index < self.get_size() and  self.pq[min_index].priority > self.pq[right_child_index].priority:
                min_index = right_child_index

            self.pq[min_index], self.pq[parent_index] = self.pq[parent_index], self.pq[min_index]

            if min_index == parent_index:
                break

            parent_index = min_index
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

    def remove_min(self):
        if self.is_empty():
            return None
        ele = self.pq[0].value
        self.pq[0] = self.pq[self.get_size() - 1]
        self.pq.pop()
        self.__percolate_down()
        return ele
        
pq = PriorityQueue()
pq.insert("A",10)
pq.insert("C",5)
pq.insert("B",19)
pq.insert("D",4)

for i in range(4):
    print(pq.remove_min())

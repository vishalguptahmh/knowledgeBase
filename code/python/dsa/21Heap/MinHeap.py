from BaseHeap import Heap

class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap)-1

        while current>0 and self.heap[current]<self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)


    def _sink_down(self, index):
        # Start at the provided index
        min_index = index
        
        # Continue until the heap property is restored
        while True:
            # Calculate indices of left and right children
            left_index = self._left_child(index)
            right_index = self._right_child(index)
    
            # If the left child exists and is less than the current node,
            # update min_index to left child's index
            if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
                min_index = left_index
    
            # If the right child exists and is less than the current smallest node,
            # update min_index to right child's index
            if (right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]):
                min_index = right_index
    
            # If the smallest value isn't at the current index,
            # swap the smallest value with the current node
            if min_index != index:
                self._swap(index, min_index)
                
                # Update the current index to the min_index
                index = min_index
            else:
                # If the smallest value is already at the current index,
                # we can stop sinking down
                return


    def remove(self):
        length = len(self.heap)
        if length ==0 : 
            return None
        if length == 1: 
            return self.heap.pop()
        
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return min_element

myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]


removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



"""
    EXPECTED OUTPUT:
    ----------------
    [6, 8, 10, 12]
    [4, 6, 10, 12, 8]
    [2, 6, 4, 12, 8, 10]

"""

"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""

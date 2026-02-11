class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def kth_smallest(self, k):
        # initialize the number of nodes visited to 0
        self.kth_smallest_count = 0
        # call the helper function with the root node and k
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            # if the current node is None, return None
            return None
 
        # recursively call the helper function on the left child of the node and store the result in left_result
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            # if left_result is not None, return it
            return left_result
 
        # increment the number of nodes visited by 1
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            # if the kth smallest element is found, return the value of the current node
            return node.value
 
        # recursively call the helper function on the right child of the node and store the result in right_result
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            # if right_result is not None, return it
            return right_result
 
        # if the kth smallest element is not found, return None
        return None
    
    # iternative
    def kth_smallest(self, k):
        # create a stack to hold nodes
        stack = []    
        # start at the root of the tree      
        temp = self.root    
        
        while stack or temp:
            # traverse to the leftmost node
            while temp: 
                # add the node to the stack                
                stack.append(temp)      
                temp = temp.left
            
            # pop the last node added to the stack
            temp = stack.pop()           
            k -= 1
            # if kth smallest element is found, return the value
            if k == 0:                  
                return temp.value
            
            # move to the right child of the node
            temp = temp.right           
            
        # if k is greater than the number of nodes in the tree, return None
        return None 



bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """
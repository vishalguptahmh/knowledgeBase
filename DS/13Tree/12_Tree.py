class Node : 
    def __init__(self,value):    
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:

    def __init__(self):
        self.root = None


    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return True
        
        temp = self.root
        while True:
            if temp.value == value:
                return False
            if temp.value > value:
                if temp.left is None:
                    temp.left = Node(value)
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = Node(value)
                    return True
                temp = temp.right

    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value == value: 
                return True
            if temp.value > value:
                temp = temp.left
            else: 
                temp = temp.right
        return False


my_tree = BinarySearchTree()
print('contains 1 : ', my_tree.contains(1))
my_tree.insert(4)
my_tree.insert(3)
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(7)




print('contains 1 : ', my_tree.contains(1))

print('contains 6 : ', my_tree.contains(6))
print('contains 68 : ', my_tree.contains(68))
print('contains 0 : ', my_tree.contains(0))
print('contains 5 : ', my_tree.contains(5))
"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        



"""
    EXPECTED OUTPUT:
    ----------------
    Root: 2
    Root->Left: 1
    Root->Right: 3

"""


##### Contains

"""


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Contains on Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.contains(5)
check(False, result, "Check if 5 exists in an empty tree:")

print("\n----- Test: Contains Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.contains(10)
check(True, result, "Check if 10 exists:")
result = bst.contains(5)
check(True, result, "Check if 5 exists:")
result = bst.contains(15)
check(True, result, "Check if 15 exists:")

print("\n----- Test: Contains Not Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.contains(15)
check(False, result, "Check if 15 exists:")

print("\n----- Test: Contains with Duplicate Inserts -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
result = bst.contains(10)
check(True, result, "Check if 10 exists with duplicate inserts:")

print("\n----- Test: Contains with Left and Right -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)
result = bst.contains(1)
check(True, result, "Check if 1 exists:")
result = bst.contains(8)
check(True, result, "Check if 8 exists:")
result = bst.contains(12)
check(True, result, "Check if 12 exists:")
result = bst.contains(20)
check(True, result, "Check if 20 exists:")

"""
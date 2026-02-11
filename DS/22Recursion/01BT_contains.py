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

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
    def r_contains(self,value):
        return self.__r_contains(self.root,value)

    def __r_contains(self,root,value):
        if root is None:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.__r_contains(root.left,value)
        if value > root.value:
            return self.__r_contains(root.right,value)

    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root,value)

    #  this will not add dublicate values
    def __r_insert(self,root,value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left =  self.__r_insert(root.left,value)
        if value> root.value:
            root.right = self.__r_insert(root.right,value)
        return root

    def __printBT(self,node):
        if node is None:
            return
        print(node.value)
        self.__printBT(node.left)
        self.__printBT(node.right)

    def printBT(self):
        self.__printBT(self.root)

        
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.r_insert(27)
my_tree.r_insert(52)
my_tree.insert(82)

my_tree.printBT()
print('\nBST Contains 27:')
print(my_tree.r_contains(27))
print('\nBST Contains 17:')
print(my_tree.r_contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
                  
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self,root):
        if root is None:
            return None
        
        righttree = root.left
        root.left = self.__invert_tree(root.right)
        root.right = self.__invert_tree(righttree)
        return root
    
    def __invert_treeBook(self, node):
        # Check if the current node is None. This happens when the tree is empty
        # or we've reached a leaf node's child. It's the base case for our recursion.
        if node is None:
            return None
        
        # Before swapping, save the original left child of the node in a temporary
        # variable. This is crucial because we're about to overwrite node.left with
        # the inverted right subtree, and we need to preserve the original left subtree
        # for inverting it next.
        temp = node.left
    
        # Recursively invert the right subtree of the current node and assign it
        # to the left child of the current node. This begins the process of swapping
        # the left and right children of the node.
        node.left = self.__invert_tree(node.right)
    
        # Now, invert the original left subtree (which we've saved in temp) and assign
        # it to the right child of the current node. This completes the swapping process.
        # Note that we use the preserved original left subtree for this, ensuring that
        # each child is correctly inverted and placed.
        node.right = self.__invert_tree(temp)
        
        # Return the current node. Now that its children have been swapped (inverted),
        # it's part of the newly inverted tree structure. This return statement allows
        # the recursion to work its way up, inverting each node's children from the bottom
        # of the tree to the top.
        return node


#  +====================================================+  
#  |  Test code below will print output to "User logs"  |
#  +====================================================+ 

def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result

def test_invert_binary_search_tree():
    print("\n--- Testing Inversion of Binary Search Tree ---")
    # Define test scenarios
    scenarios = [
        ("Empty Tree", [], []),
        ("Single Node", [1], [1]),
        ("Tree with Left Child", [2, 1], [2, None, 1]),
        ("Tree with Right Child", [1, 2], [1, 2]),
        ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
        ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
    ]

    for description, setup, expected in scenarios:
        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)
        if description == "Invert Twice":
            bst.invert()  # First inversion
        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)
        print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
        print(f"Expected: {expected}")
        print(f"Actual:   {result}")

test_invert_binary_search_tree()